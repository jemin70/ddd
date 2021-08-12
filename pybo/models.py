from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True,blank=True)


    def __str__(self):
        return self.subject
#ForeignKey는 다른 모델과 연결하기 위해 사용한다.

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True,blank=True)

class Comment(models.Model):
    #작성자
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #댓글 내용
    content = models.TextField()
    #작성 날짜
    create_date = models.DateTimeField()
    #수정날짜 - 없을 수 있음
    modify_date = models.DateTimeField(null=True, blank=True)
    #댓글이 달린 질문
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    #댓글이 달린 답변
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
