
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


ROOT_URLCONF = 'root.urls'
WSGI_APPLICATION = 'root.wsgi.application'
ASGI_APPLICATION = 'root.asgi.application'

FLATPAGE_URL = 'org'  # without leading or trailing slash

APPEND_SLASH = True

FILE_UPLOAD_PERMISSIONS = 0o664

