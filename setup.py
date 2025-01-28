import setuptools

with open("README.md", "r" , encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End_to_End_machine_learning_with_MLFlow"
AUTHOR_USER_NAME = "rushikesh092002"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "rushikeshgaikhe09@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "End-to-end machine learning pipeline using MLflow",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Buf Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages = setuptools.find_packages(where="src")
)