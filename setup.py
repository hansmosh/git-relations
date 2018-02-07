"""Get related files based on git history

See:
    https://github.com/hansmosh/git-relations
"""

from setuptools import setup

setup(
    name='git-relations',
    packages=['gitrelations'],

    version='0.2.1',

    author='Chris Brackert',
    author_email='cbrackert@gmail.com',
    url='https://github.com/hansmosh/git-relations',

    entry_points={
        'console_scripts': [
            'git-relations=gitrelations.main:main',
        ],
    },
)
