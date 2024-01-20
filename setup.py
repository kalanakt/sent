from setuptools import setup, find_packages

with open("readme.md", "r") as fh:
    long_description = fh.read()

setup(
    name='sent',
    version='0.0.23',
    packages=find_packages(),
    install_requires=['requests', 'six', 'pillow'],
    url='https://github.com/kalanakt/sent',
    author='kalanakt',
    author_email='e19198@eng.pdn.ac.lk',
    description='A package for sending Telegram messages',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='telegram api',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Communications :: Chat',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=2.4',
    project_urls={
        'Documentation': 'https://github.com/kalanakt/sent/docs',
        'Source': 'https://github.com/kalanakt/sent',
        'Tracker': 'https://github.com/kalanakt/sent/issues',
    }
)
