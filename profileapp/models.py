from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # 장고에서 제공하는 User를 객채로 받아옴
    # on_delete: 삭제 됐을때 실행 됨
        # CASCADE: 연결되어있는(종속되어있는) 것도 삭제 -> 게시글 등 관련된 것 모두 삭제
        # SET_NULL: 삭제 되었을때 User를 Null로 바꿈
    # related_name: 접근하는 방식(연결고리)  ex)target_user.profile
    image = models.ImageField(upload_to='profile/', null=True)
    # upload_to: 사진의 저장 경로
    # null: 없어도 됨(True)
    nickname = models.CharField(max_length=30, unique=True, null=True)
    # CharField : 문자열
    # unique: 고유한 값이어야 함
    message = models.CharField(max_length=200, null=True)