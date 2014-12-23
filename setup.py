import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-crumbs-mixin',
    version='0.1.5.1',
    packages=['crumbs'],
    include_package_data=True,
    license='BSD License',
    description='Put short description here...',
    long_description=README,
    url='http://github.com/bashu/django-crumbs-mixin',
    author='Basil Shubin',
    author_email='basil.shubin@gmail.com',
    install_requires=[
        'django-breadcrumbs>=1.1.3-p1',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe=False,
)
