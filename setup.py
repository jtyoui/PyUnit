from setuptools import setup, find_packages

setup(
    name='jtyoui',
    version='19.2.2',
    description='This is my collection bag.',
    url='https://github.com/jtyoui/Jtyoui',
    author='Jtyoui',
    author_email='jtyoui@qq.com',
    license='MIT Licence',
    packages=find_packages(),
    platforms="window10",
    package_data={'': ['*']},
    install_requires=['PyQt5', 'PyMuPDF', 'requests', 'pygame', 'fake_useragent', 'itchat'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False
)
