from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name="hello_world"),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),  # as_view: 이 파이썬 내에서 정상적으로 사용할수있게 해줌
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),  # primary key를 가지고잇는 id를 가져온다 ?
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update')
]
