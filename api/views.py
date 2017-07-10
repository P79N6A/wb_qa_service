#encoding:utf-8

import json
import logging
import platform
import urllib

import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api import config
from utils.resource import memory_stat, disk_stat

logger = logging.getLogger(__name__)


class Retrun2SCM(APIView):
    def get(self, request, format=None):

        try:
            params = request.query_params
            if not params or 'jobName' not in params or 'buildId' not in params:
                error_msg = {"msg": "parameter jobName and buildId are required"}
                logger.error(error_msg['msg'])
                return Response(error_msg, status=status.HTTP_400_BAD_REQUEST)
            jobName = str(params['jobName']).strip()
            buildId = str(params['buildId']).strip()

            #获取运行结果
            build_home = config.JENKINS_HOME + '/job/' + jobName + '/' + buildId
            build_res_url = build_home + '/api/json'
            build_res = urllib.urlopen(build_res_url).read()
            if 'TestResultAction' not in build_res:
                error_msg = 'no test results for the request, jobName:%s, buildId:%s' % (jobName, buildId)
                logger.error(error_msg)
                return Response(error_msg, status=status.HTTP_400_BAD_REQUEST)
            json_res = json.loads(build_res, 'UTF-8')

            # 解析运行结果 并 回调给SCM
            origin_Status = json_res['result'].lower()
            if origin_Status == 'success':
                testStatus = 'success'
            else:
                testStatus = 'fail'
            testLog = build_home + '/consoleText'
            testInfo = {'total': 0, 'fail': 0}
            for obj in json_res['actions']:
                if '_class' in obj and obj['_class'] == 'hudson.tasks.junit.TestResultAction':
                    if 'totalCount' not in obj or 'failCount' not in obj:
                        logger.error('can not find testInfo message, jobName:%s, buildID:%s' % (jobName, buildId))
                        break
                    testInfo['total'] = obj['totalCount']
                    testInfo['fail'] = obj['failCount']
                    break
            build_params = {}
            for obj in json_res['actions']:
                if '_class' in obj and obj['_class'] == 'hudson.model.ParametersAction':
                    for o in obj['parameters']:
                        build_params[o['name']] = o['value']
            if 'pipelineCaseId' not in build_params or 'nodeCaseId' not in build_params:
                error_msg = 'miss parameter pipelineCaseId or nodeCaseId when trigger preview api, jobName:%s, buildID:%s' % (jobName, buildId)
                logger.error(error_msg)
                return Response(error_msg, status=status.HTTP_400_BAD_REQUEST)

            values = {'testStatus': testStatus,
                      'testLog': testLog,
                      'testInfo': testInfo,
                      'pipelineCaseId': build_params['pipelineCaseId'],
                      'nodeCaseId': build_params['nodeCaseId']
                      }
            logger.info(json.dumps(values))
            response = requests.get(config.CALLBACK_SCM, params=values)
            json_response = json.loads(response.content)
            if response.status_code != status.HTTP_200_OK:
                error_msg = 'call back to scm error, bad request!'
                logger.error(error_msg)
                return Response(error_msg, status=status.HTTP_400_BAD_REQUEST)
            if json_response['result'] != 'success':
                error_msg = '%s jobName:%s, buildId:%s %s' % ('call back to scm error.', jobName, buildId, json_response['message'])
                logger.error(error_msg)
                return Response(error_msg, status=status.HTTP_400_BAD_REQUEST)
            if json_response['result'] == 'success':
                error_msg = '%s jobName:%s, buildId:%s %s' % ('call back to scm sucess.', jobName, buildId, json_response['message'])
                logger.info(error_msg)
                return Response(error_msg, status=status.HTTP_200_OK)

        except Exception, e:
            logger.error(e.message)
            return Response(e.message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PreviewTrigger(APIView):
    def get(self, request, format=None):

        try:
            params = request.query_params
            if 'model' not in params or 'buildType' not in params or 'host' not in params or 'nodeCaseId' not in params or 'pipelineCaseId' not in params:
                error_msg = 'the follwoing parameters are required: model、buildType、host、nodeCaseId、pipelineCaseId.'
                logger.error(error_msg)
                return Response({'result': 'fail', 'message': error_msg}, status=status.HTTP_400_BAD_REQUEST)

            if 'port' not in params:
                port = config.PREVIEW_SERVICE_PORT      # 请求不携带port参数,默认使用8080
            else:
                port = int(params['port'])
            model = str(params['model']).strip()

            values = {
                # 'model': str(params['model']),
                'buildType': str(params['buildType']).strip(),
                'host': str(params['host']).strip().split(':')[-1],
                'port': port,
                'nodeCaseId': int(params['nodeCaseId']),
                'pipelineCaseId': int(params['pipelineCaseId']),
                'token': config.TOKEN,                 #触发jenkins时需要携带密钥token,token错误触发失败
                'callBack': config.CALL_BACK
            }
            if 'users' in params:
                values['emailUsers'] = str(params['users']).strip()

            url = config.JENKINS_HOME + '/job/' + model + '/buildWithParameters'
            logger.info('trigger jenkins, url: %s, parameters: %s' % (url, values))
            response = requests.get(url, params=values, auth=(config.JENKINS_USER, config.JENKINS_PASSWORD))
            if response.status_code != status.HTTP_201_CREATED:
                logger.error(response.content)
                return Response({'result': 'fail', 'message': 'trigger jenkins fail'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            sucess_msg = {'result': 'success', 'message': 'the results will be back to you after the end of the preview'}
            logger.info(sucess_msg)
            return Response(sucess_msg, status=status.HTTP_200_OK)

        except Exception, e:
            logger.error(e.message)
            if 'invalid literal for int() with base 10' in e.message:
                return Response({'result': 'fail', 'message': 'parameter nodeCaseId、 pipelineCaseId and port must be numeric'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'result': 'fail', 'message': 'trigger preview fail'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Health(APIView):
    def get(self, request, format=None):

        results = {'results': 'success'}

        try:
            if 'Linux' in platform.system():
                mem = {}
                memory = memory_stat()
                if 'MemFree' in memory:
                    mem['MemFree'] = memory['MemFree']
                if 'Buffers' in memory:
                    mem['Buffers'] = memory['Buffers']
                if 'Cached' in memory:
                    mem['Cached'] = memory['Cached']
                results['memory'] = mem
                results['disk'] = disk_stat()

            return Response(results, status=status.HTTP_200_OK)

        except Exception, e:
            logger.error(e.message)
            return Response(results, status=status.HTTP_200_OK)
