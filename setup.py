import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BAAlgorithmUtils",
    version="3.4.4",
    author="BenArvin",
    author_email="benarvin93@outlook.com",
    description="Algorithm utils for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BenArvin/BAAlgorithmUtils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
