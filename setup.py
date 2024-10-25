from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME= "MAINA DAVIS"
SRC_REPO= "src"
LIST_OF_REQUIREMENTS= ["streamlit"]

setup(
    name = SRC_REPO,
    version= '0.0.1',
    author= AUTHOR_NAME,
    author_email= 'davismyner202@gmail.com',
    description= "Simple python web app package",
    long_description= long_description,
    long_description_content_type= 'text/markdown',
    #url="https://github.com/yourusername/yourproject",
    packages=[SRC_REPO],
    python_requires='>=3.12',
    install_requires= LIST_OF_REQUIREMENTS,
)