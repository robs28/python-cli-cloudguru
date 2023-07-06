from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()
setup(
    name='pgpackup',
    version='0.1.0',
    author='Roberto Castellanos',
    author_email='roberto.castellanos@uvltd.tech',
    description='A utility for backing up PostgreSQL databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/robs28/pgbackup',
    packages=find_packages('src')
)
