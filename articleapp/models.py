from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)
    # on_delete : 연결된 user가 삭제되었을때 경로 -> set_null: 작성자 미상
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                                related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    # media 폴더의 article 폴더에 image 저장됨
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    # 작성 시간 자동입력

    like = models.IntegerField(default=0)