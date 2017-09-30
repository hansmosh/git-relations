"""Get related files based on git history

See:
    https://github.com/hansmosh/gitrelations
"""

from setuptools import setup

setup(
    name='gitrelations',
    packages=['gitrelations'],

    version='0.1.2',

    author='Chris Brackert',
    author_email='cbrackert@gmail.com',
    url='https://github.com/hansmosh/gitrelations',

    entry_points={
        'console_scripts': [
            'gitrelations=gitrelations.main:main',
        ],
    },
)
