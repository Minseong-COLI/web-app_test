from .base import *

# env_list = dict()
#
# local_env = open(os.path.join(BASE_DIR, '.env'))
# # os: 운영체제, path: 경로, join: 합치기 메서드, base_dir: settings.py의 부모+부모 경로->venv 폴더, .env 파일을 경로지정
#
# while True:
#     line = local_env.readline()
#     if not line:
#         break
#     line = line.replace('\n','')       # 줄바꿈->공백으로 치환
#     start = line.find('=')             # =의 위치를 파악해서 그 index를 start라는 변수 에 저장
#     key = line[:start]                 # start('=')를 기준으로 슬라이싱-> key, value 지정
#     value = line[start:]
#     env_list[key] = value              # env_list 딕셔너리에 key, value 값 저장

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

def read_secret(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.lstrip().rstrip()
    file.close()
    return secret

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = read_secret('DJANGO_SECRET_KEY')

# SECRET_KEY = env_list['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': read_secret('MARIADB_USER'),
        'PASSWORD': read_secret('MARIADB_PASSWORD'),
        'HOST': 'mariadb',
        'PORT': '3306',
        # mariadb의 기본 포트: 3306
    }
}
