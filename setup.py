import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BAAlgorithmUtils",
    version="1.0.12",
    author="BenArvin",
    author_email="niedongsen@yeah.net",
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