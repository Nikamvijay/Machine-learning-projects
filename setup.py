from setuptools import setup
from typing import List



#Declaring variables for steup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Vijay Nikam"
DESRCIPTION="This  is a first Machine Learning  Projects"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    '''
    Description: This funcuon is going to returnlist of requirement mentions in requirements.txt fiel

    return This function is going to return a list which contain name of libraries mentioned in requirements.txt file
    '''
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)


