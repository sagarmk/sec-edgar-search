from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="secpanda",
    version="0.0.1",
    author="Sagar Mk",
    author_email="sagarmk@github.com",
    description="simple package to download few samples from sec ed based on agreement type",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sagarmk/sec-edgar-search.git",
    project_urls={
        "Bug Tracker": "https://github.com/sagarmk/sec-edgar-search.git/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    packages=find_packages(include=['secpanda', 'secpanda.*']),
    python_requires=">=3.7",
)

