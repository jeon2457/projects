from django.urls import path
from .views import base_views, question_views, answer_views


app_name = 'pybo'  # 별칭사용 중복에러 방지하기위함.


urlpatterns = [
    # base_views.py
    path('',
         base_views.index, name='index'),  # 추가변경
    path('<int:question_id>/',
         base_views.detail, name='detail'),  # 추가변경

    # question_views.py
    path('question/create/',
         question_views.question_create, name='question_create'),  # 질문등록하기 버튼에 사용
    path('question/modify/<int:question_id>/',
         question_views.question_modify, name='question_modify'),  # 질문수정
    path('question/delete/<int:question_id>/',
         question_views.question_delete, name='question_delete'),  # 질문삭제

    # answer_views.py
    path('answer/create/<int:question_id>/',
         answer_views.answer_create, name='answer_create'),  # URL매핑을 등록
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),  # 답변수정
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),   # 답변삭제
    path('question/vote/<int:question_id>/',
         question_views.question_vote, name='question_vote'),  # 질문추천
    path('answer/vote/<int:answer_id>/',
         answer_views.answer_vote, name='answer_vote'),  # 답변추천


]
