DATABASES = {
<<<<<<< HEAD
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "EMOJIDB",
        "USER": "root",
        "PASSWORD": "1234",
        "HOST": "localhost",
        "PORT": "3306",
=======
    'default': {
        # 1. 사용할 엔진 설정
        'ENGINE': 'django.db.backends.mysql',
        # 2. 연동할 MySQL의 데이터베이스 이름
        'NAME': 'emojis_db',
        # 3. DB 접속 계정명  / 연결할 db에 따라 다를 수 있음
        # 'USER': 'kwbin',
        'USER': 'kwb',
        # 4. DB 패스워드
        'PASSWORD': '0000',
        # 5. DB 주소 / 연결할 db에 따라 다를 수 있음
        'HOST': 'localhost',
        # 6. 포트번호
        'PORT': '3306',
>>>>>>> cdb81bf9dfea302e2301f755250ae452be11be4f
    }
}
SECRET_KEY = "django-insecure-x7tzy4(-4bj$hlf40tq+rk4w=^pc_vr$c*yy7)s5gypa&s^88i"
# SECRET_KEY = "django-insecure-%4q1jlt5)_5jh!8t*g#z9=u#@!2l+5i2!_jueemek5r4vd(9+_"
