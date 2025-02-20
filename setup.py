from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''this function returns a list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  ## read the lines in requirements.txt file
        requirements = [req.replace("\n", "") for req in requirements]  ## remove the \n from the requirements
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  ## remove the -e . line

    return requirements

## metadata information about entire project
setup(
    name='mlproject',
    version='0.0.1',
    author='Vinay',
    author_email='vinayjpr40@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  ## this function takes library from requirements.txt and installs it
)