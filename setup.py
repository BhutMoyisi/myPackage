from setuptools import setup, find_packages

setup(
    name="myPackage",
    version="0.1.0",
    packages=find_packages(exclude=["Tests*"]),
    license="MIT",
    description="A sample Python package",
    long_description=open("README.md").read(),
    install_requires=['numpy'],  # example dependency
    url='https://github.com/<username>/<package-name>',
    author='<Your Name>',
    author_email='<Your Email>'
)
