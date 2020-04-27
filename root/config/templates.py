import os

from root.config.base_dir import BASE_DIR

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'html'),
]

TEMPLATE_LOADERS = (
    'tenant_schemas.template_loaders.FilesystemLoader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'lib.context_processors._settings',
                'lib.context_processors.terms',
            ],
        },
    },
]


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)