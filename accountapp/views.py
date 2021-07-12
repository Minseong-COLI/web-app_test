from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        # 객체를 DB에 저장    # temp와 다르게 DB에 저장됨(왼쪽 파일 목록 db.sqlite3)
        # settings.py의 DATABASE 내용 확인 해보면 지정된걸 확인할수있음

        return render(request, 'accountapp/hello_world.html',
                      context={'new_hello_world': new_hello_world})
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'text': 'GET METHOD!'})

