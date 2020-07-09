from setuptools import setup, find_packages

from jtyoui import __version__, __author__, __description__, __email__

with open('README.md', encoding='utf-8') as f:
    long_text = f.read()

with open('requirements.txt', encoding='utf-8') as f:
    install_requires = f.read().strip().splitlines()

setup(
    name=__author__.lower(),
    version=__version__,
    description=__description__,
    long_description=long_text,
    long_description_content_type="text/markdown",
    url='https://github.com/jtyoui/Jtyoui',
    author=__author__,
    author_email=__email__,
    license='MIT Licence',
    packages=find_packages(),
    platforms=["window10", "Linux"],
    package_data={'': ['*']},
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False
    # entry_points={"console_scripts": ["jtyoui = jtyoui.cli:main"]}
)
