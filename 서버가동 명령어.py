
# 로컬환경에서 장고 서버를 동작할 때 사용한다.
# python manage.py runserver --settings=config.settings.local
#


'''
# AWS 서버환경에서 장고 서버를 동작할 때는
# 2. python manage.py runserver --settings=config.settings.prod
'''


'''

# 로컬 설정 자동화(환경변수 이용)
# set DJANGO_SETTINGS_MODULE=config.settings.local
# python manage.py runserver
# ==>>  실행하면 "CommandError: You must set settings.ALLOWED_HOSTS if DEBUG is False."라고
# 계속해서 에러가 나는데 해결책을 못찾고있다. ㅠㅠ

'''

# [엑셀문서, 그대로 웹에 게시하는 방법]
# https://s-eight.tistory.com/entry/%EC%97%91%EC%85%80%EB%AC%B8%EC%84%9C-%EA%B7%B8%EB%8C%80%EB%A1%9C-%EC%82%AC%EC%9D%B4%ED%8A%B8%EC%97%90-%EA%B2%8C%EC%8B%9C%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-html
