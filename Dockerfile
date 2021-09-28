FROM python:3.9.0

WORKDIR /home/
# ubuntu에 있는 home 경로

RUN echo "asdfqwQWER"
# 코드가 변경될때마다 run echo를 앞에 입력해주면 run echo 아래로부터는 변경된 내용 반영됨

RUN git clone https://github.com/Minseong-COLI/web-app_test.git
# git hub 소스코드를 복제

WORKDIR /home/web-app_test
# 위 git hub 소스코드의 마지막 경로와 일치 시켜주기

RUN #echo "SECRET_KEY=django-insecure-3&1ujxrsg353so%&$+q__2o$-*9_xnp$e($7@(c(q!$wiqgvzr" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

#RUN python manage.py migrate --settings=coli_20210629.settings.deploy
## settings를 통해 배포환경 기반 설정을 해준다
#
#RUN python manage.py collectstatic --noinput --settings=coli_20210629.settings.deploy
## settings를 통해 배포환경 기반 설정을 해준다
## collecstatic --noinput을 사용해서 portainer에서 실행했을때 멈추지 않도록(yes/no 묻지않도록) 해준다.

EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# CMD를 gunicorn 명령어로 변경
CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=coli_20210629.settings.deploy && python manage.py migrate --settings=coli_20210629.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=coli_20210629.settings.deploy coli_20210629.wsgi --bind 0.0.0.0:8000"]
# coli_20210629 -> mainapp 폴더명