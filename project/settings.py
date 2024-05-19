from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-)949z$(tri&sw-*mq365*x1)6c5*wk_qb8v($rpih%l#4x6&xx'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
    'crispy_forms',
    'crispy_bootstrap4',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CLIENT_CERTIFICATE = """
Certificate:
    Data:
        Version: 1 (0x0)
        Serial Number: 390578 (0x5f5b2)
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=RU, ST=Ufa, L=Ufa, O=slb, CN=slb/emailAddress=support@slb.medv.ru
        Validity
            Not Before: Apr 22 10:45:30 2024 GMT
            Not After : Apr 22 10:45:30 2025 GMT
        Subject: C=RU, ST=Moscow, L=Moscow, O=Test, CN=test@test.test
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:8f:27:f7:0b:d4:34:23:c5:20:d3:f0:40:f7:8e:
                    1d:ad:f7:c3:fe:63:e4:c8:3d:52:d8:1e:98:08:23:
                    df:5d:09:c4:be:72:0f:57:9c:fa:88:0d:2e:7d:ae:
                    16:4c:62:a0:b1:50:21:01:ee:d9:33:e1:b0:07:3f:
                    1b:c4:04:40:28:43:18:ad:7a:83:a3:b6:0c:c8:f3:
                    46:65:d6:6d:6e:a6:6a:ad:01:dc:56:8f:0f:c6:d0:
                    e0:42:f9:85:be:af:46:87:77:32:70:00:7b:e5:9f:
                    0a:6d:34:e6:61:32:85:3f:60:51:8f:69:5f:c6:f4:
                    73:ee:48:82:51:53:21:3a:5f:d5:9f:cd:0e:5f:7c:
                    82:73:88:4b:c0:b3:9d:38:9d:4e:8a:fb:a4:af:48:
                    3e:82:6a:b9:77:a3:d2:41:e4:81:db:b3:53:68:90:
                    0d:c5:c7:45:19:90:ac:a1:76:f0:61:4c:82:86:41:
                    f9:63:25:af:57:0b:4a:c4:e7:a7:aa:f8:03:4e:84:
                    81:e0:73:6c:9e:09:4b:30:72:11:7f:be:30:03:a0:
                    f7:dc:a0:e4:28:e6:78:f8:6f:1a:49:54:0b:ee:01:
                    e9:4d:30:50:15:d1:f6:92:33:6a:c5:81:ca:84:3f:
                    aa:5f:14:19:ce:fd:23:45:50:c9:63:c4:51:5d:70:
                    ed:91
                Exponent: 65537 (0x10001)
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        03:55:e6:e6:88:89:1c:08:3f:0e:9b:b9:7f:e7:41:fa:fe:51:
        44:98:61:d3:f0:c0:0f:57:8b:d6:6e:18:b5:65:2c:39:df:a9:
        ec:76:89:5d:28:e7:c9:b4:3f:3a:4e:85:6a:c8:6c:e2:5e:fd:
        15:ea:79:b1:e7:e6:36:fc:8c:4e:9a:1f:c2:37:58:7b:ed:47:
        4c:eb:84:a1:2c:23:2c:37:b7:82:65:7f:a9:93:7c:09:cd:c4:
        65:5a:fc:1a:98:3f:50:73:6a:4f:9e:41:a0:ab:bb:33:c0:d2:
        c1:78:d2:3c:ac:71:fb:3e:3e:97:f0:77:70:eb:b4:cd:96:67:
        68:a5:2b:6d:bc:80:c2:a2:a8:5e:d7:d6:a9:02:99:99:7e:53:
        95:b6:47:c0:78:6a:dc:aa:9d:5a:ab:ae:44:de:fb:a2:4e:41:
        d9:44:00:4a:a4:c9:42:68:22:e9:25:5d:a8:4f:0a:54:29:d4:
        bf:64:88:32:84:a3:84:20:4b:2d:a2:a3:7e:28:de:24:4e:3b:
        f6:7c:8b:82:0f:9f:b0:c7:50:50:f5:7b:e2:30:3a:48:19:4c:
        08:14:9d:b0:a8:c5:5d:65:52:94:f6:c4:49:1c:1d:da:6f:ba:
        a4:26:b4:68:63:e6:ee:5c:ed:76:ef:aa:9e:fd:7d:6b:34:d6:
        40:90:5a:f1
-----BEGIN CERTIFICATE-----
MIIDNjCCAh4CAwX1sjANBgkqhkiG9w0BAQsFADBpMQswCQYDVQQGEwJSVTEMMAoG
A1UECAwDVWZhMQwwCgYDVQQHDANVZmExDDAKBgNVBAoMA3NsYjEMMAoGA1UEAwwD
c2xiMSIwIAYJKoZIhvcNAQkBFhNzdXBwb3J0QHNsYi5tZWR2LnJ1MB4XDTI0MDQy
MjEwNDUzMFoXDTI1MDQyMjEwNDUzMFowVzELMAkGA1UEBhMCUlUxDzANBgNVBAgM
Bk1vc2NvdzEPMA0GA1UEBwwGTW9zY293MQ0wCwYDVQQKDARUZXN0MRcwFQYDVQQD
DA50ZXN0QHRlc3QudGVzdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
AI8n9wvUNCPFINPwQPeOHa33w/5j5Mg9UtgemAgj310JxL5yD1ec+ogNLn2uFkxi
oLFQIQHu2TPhsAc/G8QEQChDGK16g6O2DMjzRmXWbW6maq0B3FaPD8bQ4EL5hb6v
Rod3MnAAe+WfCm005mEyhT9gUY9pX8b0c+5IglFTITpf1Z/NDl98gnOIS8CznTid
Tor7pK9IPoJquXej0kHkgduzU2iQDcXHRRmQrKF28GFMgoZB+WMlr1cLSsTnp6r4
A06EgeBzbJ4JSzByEX++MAOg99yg5CjmePhvGklUC+4B6U0wUBXR9pIzasWByoQ/
ql8UGc79I0VQyWPEUV1w7ZECAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAA1Xm5oiJ
HAg/Dpu5f+dB+v5RRJhh0/DAD1eL1m4YtWUsOd+p7HaJXSjnybQ/Ok6Fashs4l79
Fep5sefmNvyMTpofwjdYe+1HTOuEoSwjLDe3gmV/qZN8Cc3EZVr8Gpg/UHNqT55B
oKu7M8DSwXjSPKxx+z4+l/B3cOu0zZZnaKUrbbyAwqKoXtfWqQKZmX5TlbZHwHhq
3KqdWquuRN77ok5B2UQASqTJQmgi6SVdqE8KVCnUv2SIMoSjhCBLLaKjfijeJE47
9nyLgg+fsMdQUPV74jA6SBlMCBSdsKjFXWVSlPbESRwd2m+6pCa0aGPm7lztdu+q
nv19azTWQJBa8Q==
-----END CERTIFICATE-----
"""

CLIENT_KEY = """
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCPJ/cL1DQjxSDT
8ED3jh2t98P+Y+TIPVLYHpgII99dCcS+cg9XnPqIDS59rhZMYqCxUCEB7tkz4bAH
PxvEBEAoQxiteoOjtgzI80Zl1m1upmqtAdxWjw/G0OBC+YW+r0aHdzJwAHvlnwpt
NOZhMoU/YFGPaV/G9HPuSIJRUyE6X9WfzQ5ffIJziEvAs504nU6K+6SvSD6Carl3
o9JB5IHbs1NokA3Fx0UZkKyhdvBhTIKGQfljJa9XC0rE56eq+ANOhIHgc2yeCUsw
chF/vjADoPfcoOQo5nj4bxpJVAvuAelNMFAV0faSM2rFgcqEP6pfFBnO/SNFUMlj
xFFdcO2RAgMBAAECggEABkbA9L/Prrx3J/5MmuNG4dhkZhmIb6Rgpsu7QVVxTD71
ZUl9lWBzNivTHKeD9W1i5jiWeeM4RVILybA2o21xnVJJGVyvENUWfROiw9bsOAG2
g5ylRcDtTCY0RDt0ZbEsQnGIwJME25hmzfWXyYMm3GnN/vT7wgP4YTtvRemDIhqo
vgfJ92yhKhlLhbYL4ivcmsCajaBFN4PI/1RdubguCGTTbLKQaK4hjcsNWifut4cg
WUTPwzNwtyATYOq2JcCTKNEcWMrz9q9sMoXgUciOH1jG6b82B5yMUqjSvPVsz/AC
lNgVt1lyEJs3RSWy4iVOyQx5z+VhCsdmBcLGJxUoUQKBgQDF2dJz8jufCzi92beW
1OE2GcwWaUD0ut7cHMbMCs5iUKaTKrmgFW57mMfzRpUdTtE/ta/zWKbJlTQiereL
qsR937WTt2XUFtpwGMHgUVId/hUu/IFbs6b11IwFOJfbApGVLYr5372bqrectmAG
qdiPPIRBkZG6oHxAkSBxucUvGwKBgQC5OvF01t3/6ZOY63pHeBI2BsIH1pYP8jkF
HGAUDAg/F1Psp0SR/PrcKQ97eYkCCzCNBoSgeLA0SehHNNtBYSG9YR98x9LYLJko
Io0h4yXfL9DXBk3h5Uc9XDY7ZU0y78LI0k+yNTQvPjUiQFhJ3bZCIH1LrJBFHEwW
jxguHX7kwwKBgD6EzxiuUaK3JA3xzy6NREEZM8FdLxZmOmfpe/Qb8g1lGM3mMVPh
kdDifURlaFcjgcGVAu1tdP679AZ1KqyqoH56A2GTEU1Mj2femtzsNXuev0jip2m3
wilqKXi44ltlW2V9R64fwkV/U5fklUFlyDWy1MP3YMpNThYFBfCJ2EJDAoGBAKl8
E38zM8J7uP/NRv+qEA+7M0L0yC4jFqVkh00QjWMdNz9s9cMW1XspXu8+D2z9TBle
A3DJvYC6t3ygEpbKB5M/EQ6d0IDYnfMpWjXNn9ON7usw64ZswjiU7VJ/qJmY5IPY
W+/V2r/3jaqfcal04tWy4LKjXQa/k6d4m0lm17r9AoGBAJBXuJwK4ev76fZ1Y7rJ
lDAwjhme8t2dJ/aG12TNnschxAe/7LRwxRyMIu63ALhD5Air8VkdVCz+kb9P2Ny1
ZEyshP7wsIqb42cW94CzIyiLwLzT07jfu4GdNv5tekmdj5bzstreJPFIVRvfZwO/
Ar4XzwkZ3fClYyItc1jMoBIk
-----END PRIVATE KEY-----
"""
