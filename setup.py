#  to create Pypi packages we use setup.py file

import setuptools

with open("README.md", "r",encoding="utf-8") as f:

    long_description = f.read()


__Version__ = "0.0.0"

# GITHUB REPOSITORY NAME
REPO_NAME = "text-summarizer"
#  GIHUB USERNAME
AUTHOR_USER_NAME = "Amitgm"
# UNDER YOUR SOURCE FOLDER NAME
SRC_NAME = "textsummarizer"
# YOUR EMAIL ID
AUTHOR_EMAIL = "amittimer@gmail.com"

# it looks for constructor file __init__.py in every folder and install it as a local package

setuptools.setup(

    name = SRC_NAME,
    version =  __Version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A simple text summarizer for nlp applications",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",

)






