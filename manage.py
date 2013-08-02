# -*- coding: utf-8 -*-

import os

from django.core.management import execute_manager

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
        }
    }

MIDDLEWARE_CLASSES = [
    'breadcrumbs.middleware.BreadcrumbsMiddleware',
    ]

PROJECT_APPS = [
    'crumbs',
    ]

INSTALLED_APPS = [
    'breadcrumbs',

    'django_jenkins',
    ] + PROJECT_APPS

ROOT_URLCONF = 'test_urls'

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, 'test_templates'),
    ]

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
    'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.django_tests',
    )

COVERAGE_EXCLUDES_FOLDERS = ['crumbs/tests/*']
PYLINT_RCFILE = os.path.join(PROJECT_ROOT, 'pylint.rc')

if __name__ == "__main__":
    from django.conf import settings
    settings.configure(
        DATABASES = DATABASES,
        INSTALLED_APPS = INSTALLED_APPS,
        MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES,
        PROJECT_APPS = PROJECT_APPS,
        JENKINS_TASKS = JENKINS_TASKS,
        ROOT_URLCONF = ROOT_URLCONF,
        COVERAGE_EXCLUDES_FOLDERS = COVERAGE_EXCLUDES_FOLDERS,
        PYLINT_RCFILE = PYLINT_RCFILE,
        TEMPLATE_DIRS = TEMPLATE_DIRS,
        TEMPLATE_DEBUG = TEMPLATE_DEBUG,
        )
    execute_manager(settings)
