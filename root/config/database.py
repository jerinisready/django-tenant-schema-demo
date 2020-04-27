# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
import os

from root.config.base_dir import BASE_DIR

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': 5432,
    }
}


DATABASE_ROUTERS = (
    'tenant_schemas.routers.TenantSyncRouter',
)


