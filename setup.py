from setuptools import setup, find_packages

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name='sent',
    version='0.0.15',
    packages=find_packages(),
    install_requires=['requests'],
    url='https://github.com/kalanakt/sent',
    author='kalanakt',
    author_email='e19198@eng.pdn.ac.lk',
    description='A package for sending Telegram messages',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='telegram api',
    license='MIT',
)

# python setup.py sdist
# python setup.py sdist bdist_wheel
# twine upload dist/*
