from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="AnimeRecommenderProject",
    version="0.1",
    author="Jalaj",
    packages=find_packages(),
    install_requires=requirements,
)