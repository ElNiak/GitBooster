# PANTHER-SCP/panther/setup.py

import codecs
import os
from setuptools import setup, find_packages


# Get the long description from the README file
here = os.path.abspath(os.path.dirname(__file__))
try:
  with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
      long_description = f.read()
except:
  # This happens when running tests
  long_description = None
setup(
    name='GitBooster',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        "setuptools",
        'GitPython',
        'python-crontab',
    ],
    entry_points={
        'console_scripts': [
            'gitbooster=gitbooster.gitbooster:main',
        ],
    },
    author='ElNiak',
    author_email='your.email@example.com',
    description='GitBooster:  Boosts your GitHub stats with automated, scheduled commits to keep your profile active.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ElNiak/GitBooster',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
