import setuptools
from distutils.core import setup, Extension

with open("README.md") as _file:
    long_description = _file.read()

setuptools.setup(
        name= "Penguin-Services",
        version = "2.0.0",
        author = "VeteranCode",
        author_email = "jacob.h.barrow@gmail.com",
        long_description = long_description,
        long_description_content_type = "text/markdown",
        url = "",
        packages=setuptools.find_packages(),
        install_requires = [
            "dataclasses",
        ], 
        license = "MIT",
        classifiers =  [
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
        ],
)
