from setuptools import setup, find_packages

setup(
    name='sample-package',
    version='2.0.0',
    description='Sample Package',
    author='sangyeon217',
    author_email='sangyeon217@gmail.com',
    packages=find_packages(include=['sample']),
)