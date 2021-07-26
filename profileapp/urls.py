from django.urls import path

from profileapp.views import ProfileCreateView

app_name = 'profileapp'
# profileapp 폴더의 라우트 경로 지정


urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create')
]
