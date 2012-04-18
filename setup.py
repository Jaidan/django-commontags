from distutils.core import setup
from commontags import get_version

setup(
    name="django-commontags",
    version=get_version().replace(' ', '-'),
    packages=['commontags',],
    long_description=open('README').read(),
    description="Common django template tags and filters",
)
