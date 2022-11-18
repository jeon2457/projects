from .base import *  # base.py 파일의 모든 내용을 사용한다는 의미

# local.py 파일의 내용은 base.py 파일과 동일하지만 ALLOWED_HOSTS만 다르게 설정하겠다는 의미


ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # 원래는 []상태이다.
