import setuptools

# Read the README.md file for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define package information
__version__ = "0.1.0"  # Update with the actual version number
REPO_NAME = "End-to-end-ML-Project-with-MLflow"
AUTHOR_USER_NAME = "fs-dp"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "zekitekin@yahoo.com"

# Setup configuration
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for machine learning applications",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Corrected attribute name
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify the required Python version
)