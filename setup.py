"""
Setup configuration for 2526_B3_S6_Projet
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="2526_B3_S6_Projet",
    version="0.1.0",
    author="B3 S6 Team",
    description="Python project for B3 S6 course",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
