import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

from jinja2_gtm import __version__

setup(
    name = "django-jinja2-gtm",
    version = __version__,
    author = "Damien Barchowsky",
    author_email = "dbarchowsky@gmail.com",
    description = ("Jinja2 macro for injecting Google Tag Manager code in templates."),
    license = "MIT",
    keywords = "django jinja2 generic-views",
    url = "https://github.com/dbarchowsky/django-jinja2-gtm",
    packages=find_packages(),
    include_package_data=True,
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
