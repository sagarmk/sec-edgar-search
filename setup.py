import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="secpanda-SAGAR_MK",
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
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)