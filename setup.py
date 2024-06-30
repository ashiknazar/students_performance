from setuptools import setup, find_packages
from typing import List

# Constant for editable install
EDITABLE_INSTALL = '-e .'

def get_requirements(filepath: str) -> List[str]:
    """
    Reads a requirements file and returns a list of dependencies.
    
    Args:
        filepath (str): Path to the requirements file.
        
    Returns:
        List[str]: List of dependencies.
    """
    requirements = []
    with open(filepath) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if EDITABLE_INSTALL in requirements:
            requirements.remove(EDITABLE_INSTALL)
    return requirements


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='students_performance',
    version='0.0.1',
    author='Ashik Nazar',
    author_email='datas293@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    long_description=long_description,
    long_description_content_type="text/markdown",
)
