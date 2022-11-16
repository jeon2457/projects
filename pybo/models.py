from django.db import models
from django.contrib.auth.models import User  # 글쓴이 확인
# Create your models here.


class Question(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_question')  # 글쓴이 확인
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)  # 수정일시 추가!
    voter = models.ManyToManyField(
        User, related_name='voter_question')  # 추천인 추가

    def __str__(self):
        return self.subject  # __str__ 메서드를 추가하면 id 값 대신 제목을 표시할 수 있다.(DB 질문제목)


class Answer(models.Model):
    # null=True (옵션)속성을 부여하면 migrate시 데이터베이스에 null 허용 컬럼으로 생성된다.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_answer')  # 글쓴이 확인
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)  # 수정일시 추가!
    voter = models.ManyToManyField(User, related_name='voter_answer')
