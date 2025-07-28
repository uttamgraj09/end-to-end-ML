import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "end-to-end-ML"
AUTHOR_USER_NAME = "UTTAMGRAJ"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "uttamgraj292@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content_type="text/markdown",  # ✅ fixed key name
    url=f"https://github.com/uttamgraj09/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/uttamgraj09/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

