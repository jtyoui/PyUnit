from setuptools import setup, find_packages

setup(
    name='jtyoui',
    version='19.1.15',
    description='This is my collection bag.',
    url='https://github.com/jtyoui',
    author='jtyoui',
    author_email='jtyoui@qq.com',
    license='MIT Licence',
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=['requests'],
    package_data={'': ['*.txt', '*.md']},
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    zip_safe=False
)
