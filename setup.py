from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='tmwad',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['requests'],
    url='https://github.com/kalanakt/tmwad',
    author='kalanakt',
    author_email='e19198@eng.pdn.ac.lk',
    description='A package for sending Telegram messages',
    long_description=long_description,
    keywords='telegram api',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

# python setup.py sdist
# twine upload dist/*
