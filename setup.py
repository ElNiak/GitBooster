# PANTHER-SCP/panther/setup.py

from setuptools import setup, find_packages

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
    url='https://github.com/ElNiak/GitBooster',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
