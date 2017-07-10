import os
from qa_service import settings

logs_dir = os.path.join(settings.BASE_DIR, 'logs')

if not os.path.exists(logs_dir):
    os.mkdir(logs_dir)