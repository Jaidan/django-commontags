from distutils.core import setup
from commontags import get_version

setup(
    name="django-commontags",
    version=get_version().replace(' ', '-'),
    packages=['commontags',],
    author="42nd Design and CREO Agency",
    long_description=open('README.rst').read(),
    description="Common django template tags and filters",
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",
    ],
    url="http://pypi.python/ord/pypi/django-commontags",
    license="LICENSE",
    install_requires=[
        "Django >= 1.1.1",
    ]
)
