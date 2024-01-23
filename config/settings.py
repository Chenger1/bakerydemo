"""
Django settings for temp project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
import dj_database_url
import environ

# Get environ instance
env = environ.Env()

# Build paths inside the project like this: os.path.join(PROJECT_DIR, ...)
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
PROJECT_DIR = BASE_DIR / "src"

# Read env file
READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
ENV_PATH = env.str("DJANGO_ENV_PATH", default=".env")
if READ_DOT_ENV_FILE:
    environ.Env.read_env(os.path.join(BASE_DIR, ENV_PATH))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("DJANGO_SECRET_KEY")
WAGTAILADMIN_BASE_URL = env.str("DJANGO_WAGTAILADMIN_BASE_URL", default="http://127.0.0.1:8000/admin/")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Uncomment this (and adjust as appropriate) to enable django-debug-toolbar
# INTERNAL_IPS = [
#     '127.0.0.1',
# ]

# Application definition

INSTALLED_APPS = [
    "django_components",
    "src.base",
    "src.blog",
    "src.breads",
    "src.locations",
    "src.recipes",
    "src.search",
    "src.tinymce_editor",
    "src.wagtailvideos",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.api.v2",
    "wagtail.locales",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.table_block",
    "wagtail.contrib.typed_table_block",
    "wagtail.contrib.search_promotions",
    "wagtail.contrib.settings",
    "wagtail.contrib.simple_translation",
    "wagtail.contrib.styleguide",
    "wagtail",
    "rest_framework",
    "modelcluster",
    "taggit",
    "wagtail_modeladmin",
    "wagtailfontawesomesvg",
    "debug_toolbar",
    "django_extensions",
    "django_vite",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
    "src.base.middleware.ExternalLinkRedirectMiddleware"
]

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "src/../templates",
            "components",
        ],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ],
            'loaders': [(
                'django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    'django_components.template_loader.Loader',
                ]
            )],
            'builtins': [
                'django_components.templatetags.component_tags',
            ]
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
CSRF_TRUSTED_ORIGINS = ["http://localhost", "https://wagtail.avada-media-dev1.od.ua"]

DJANGO_VITE_ASSETS_PATH = BASE_DIR / "static_nodejs"
DJANGO_VITE_STATIC_URL_PREFIX = "nodejs"
DJANGO_VITE_DEV_MODE = env.bool("DJANGO_VITE_DEV_MODE", True)
DJANGO_VITE_DEV_SERVER_HOST = "localhost"
DJANGO_VITE_DEV_SERVER_PORT = 3000
DJANGO_VITE_MANIFEST_PATH = DJANGO_VITE_ASSETS_PATH / "nodejs/manifest.json"

STATICFILES_DIRS = [
    BASE_DIR / "components",
    BASE_DIR / "static",
    DJANGO_VITE_ASSETS_PATH
]

STATIC_ROOT = os.path.join(BASE_DIR, "collect_static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Override in local settings or replace with your own key. Please don't use our demo key in production!
GOOGLE_MAP_API_KEY = "AIzaSyD31CT9P9KxvNUJOwDq2kcFEIG8ADgaFgw"

# Use Elasticsearch as the search backend for extra performance and better search results
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
        "INDEX": "src",
    },
}

# Wagtail settings
WAGTAIL_SITE_NAME = "bakerydemo"

WAGTAIL_I18N_ENABLED = True

WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [
    ("en", "English"),
    ("de", "Deutsch"),
    ("ar", "العربيّة"),
]

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "changeme")

# Content Security policy settings
# http://django-csp.readthedocs.io/en/latest/configuration.html

# Only enable CSP when enabled through environment variables.
if "CSP_DEFAULT_SRC" in os.environ:
    MIDDLEWARE.append("csp.middleware.CSPMiddleware")

    # Only report violations, don't enforce policy
    CSP_REPORT_ONLY = True

    # The “special” source values of 'self', 'unsafe-inline', 'unsafe-eval', and 'none' must be quoted!
    # e.g.: CSP_DEFAULT_SRC = "'self'" Without quotes they will not work as intended.

    CSP_DEFAULT_SRC = os.environ.get("CSP_DEFAULT_SRC").split(",")
    if "CSP_SCRIPT_SRC" in os.environ:
        CSP_SCRIPT_SRC = os.environ.get("CSP_SCRIPT_SRC").split(",")
    if "CSP_STYLE_SRC" in os.environ:
        CSP_STYLE_SRC = os.environ.get("CSP_STYLE_SRC").split(",")
    if "CSP_IMG_SRC" in os.environ:
        CSP_IMG_SRC = os.environ.get("CSP_IMG_SRC").split(",")
    if "CSP_CONNECT_SRC" in os.environ:
        CSP_CONNECT_SRC = os.environ.get("CSP_CONNECT_SRC").split(",")
    if "CSP_FONT_SRC" in os.environ:
        CSP_FONT_SRC = os.environ.get("CSP_FONT_SRC").split(",")
    if "CSP_BASE_URI" in os.environ:
        CSP_BASE_URI = os.environ.get("CSP_BASE_URI").split(",")
    if "CSP_OBJECT_SRC" in os.environ:
        CSP_OBJECT_SRC = os.environ.get("CSP_OBJECT_SRC").split(",")


WAGTAILIMAGES_EXTENSIONS = ["gif", "jpg", "jpeg", "png", "webp", "svg"]


WAGTAILADMIN_RICH_TEXT_EDITORS = {
    "default": {
        "WIDGET": "src.tinymce_editor.widget.TinyMCERichTextArea",
    }
}
