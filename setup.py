import setuptools

with open("README.md","r",encoding="utf-8") as f:   # this for if we publish the library in the pypi so we need to be an exaplaintion about the usage of the library
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-summarizer"
AUTHOR_USERNAME = "nourdugha"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "nouraldeendugha@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A simple Python library for summarizing text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/" + AUTHOR_USERNAME + "/" + REPO_NAME,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    )