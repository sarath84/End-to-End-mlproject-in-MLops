from setuptools import setup,find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    HYPEN_E_DOT= '-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n" , " ") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements


setup(
    name='ML-project with MLops',
    version="0.0.1",
    author='Sarath',
    author_email='acsarath650@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)  





