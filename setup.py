#!/usr/bin/env python

from setuptools import find_packages, setup

from aldryn_bootstrap3 import __version__


REQUIREMENTS = [
    'django-appconf>=1.0.0',
    'django-cms>=3.11,<3.12',
    'django-filer>=3.0',
    'djangocms-text-ckeditor>=5.1.0',
    'djangocms-attributes-field>=3.0.0',
]


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Framework :: Django :: 4.2',
    'Framework :: Django CMS :: 3.11',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
]


setup(
    name='aldryn-bootstrap3',
    version=__version__,
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/aldryn/aldryn-bootstrap3',
    license='BSD',
    description=('Adds Bootstrap 3 components as plugins.'),
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    python_requires='>=3.9',
    classifiers=CLASSIFIERS,
    test_suite='tests.settings.run',
)
