from setuptools import setup, find_packages

setup(
    name='tmwad',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['requests'],
    url='https://github.com/kalanakt/tmwad',
    author='kalanakt',
    author_email='e19198@eng.pdn.ac.lk',
    description='A package for sending Telegram messages',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
)
