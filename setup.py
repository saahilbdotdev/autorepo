import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="autorepo",
    version="0.1.4",
    description="AutoRepo is a simple, cli-based tool for creating github repositories, without leaving your terminal!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/XanderWatson/autorepo",
    author="Saahil Bhavsar",
    author_email="saahil_bhavsar@outlook.com",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Version Control :: Git",
        "Topic :: Utilities"
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    install_requires=["click", "keyring", "pygithub"],
    entry_points={
        "console_scripts": [
            "repo=autorepo:autorepo",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/XanderWatson/autorepo/issues",
        "Funding": "https://buymeacoffee.com/saahilb",
        "Source": "https://github.com/XanderWatson/autorepo",
    },
)
