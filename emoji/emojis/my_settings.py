DATABASES = {
    'default': {
        # 1. 사용할 엔진 설정
        'ENGINE': 'django.db.backends.mysql',
        # 2. 연동할 MySQL의 데이터베이스 이름
        'NAME': 'emojis_db',
        # 3. DB 접속 계정명  / 연결할 db에 따라 다를 수 있음
        'USER': 'kwb',
        # 4. DB 패스워드
        'PASSWORD': '0000',
        # 5. DB 주소 / 연결할 db에 따라 다를 수 있음
        'HOST': 'localhost',
        # 6. 포트번호
        'PORT': '3306',
    }
}
SECRET_KEY = "django-insecure-%4q1jlt5)_5jh!8t*g#z9=u#@!2l+5i2!_jueemek5r4vd(9+_"
