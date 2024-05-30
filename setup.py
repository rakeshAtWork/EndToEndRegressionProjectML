from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'  # this things has been defined in the requirement.txt file, the use of this is to trigger the setup.py file when it will reun requirements.txt file.


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='RegressorProject',
    version='0.0.1',
    author='Rakesh',
    author_email='rakros252525@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
