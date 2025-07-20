from setuptools import find_packages,setup
from typing import List
HYPHEN_e_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    requirements = []
    try:
        with open(file_path,'r') as file_obj:
            requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]
        if HYPHEN_e_DOT in requirements:
            requirements.remove(HYPHEN_e_DOT)
        return requirements
    except Exception as e:
        print(e)

setup(
    name="networksecurity",
    version="0.0.1",
    author="rahul bc",
    author_email="rahulbc17@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)