from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """

    Returns:
        List of requirements mentioned in the requirements.txt file
    """
    requirements:List[str]= []
    with open('requirements.txt') as f:
        for line in f.readlines():
            requirements.append(line)
    return requirements



setup(
    name="sensor",
    version="1.0.0",
    description="sensor package is a simple package for interacting with sensor data",
    author="Pranay",
    author_email="pranaynaik007@hotmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)


