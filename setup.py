from setuptools import setup,find_packages
from typing import List
HYPEN_E_DOT = '-e .'
def get_requirements()->List[str]:
    try:
        requirements = []
        with open("requirements.txt",'r') as file:
            lines = file.readlines()
            requirements = [requirements.replace("\n","") for requirements in lines]
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
            return requirements
    except Exception as e:
        print(e)

setup(
    name='neworksecurity',
    version= '0.0.1',
    author='rahul b c',
    author_email= 'rahulbc17@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements()
)
