from setuptools import find_packages, setup
from typing import List

def get_Requirements(file_path: str) -> list[str]:

    ''' 
    this function will return the list of requirements
    
    '''
    requirements=[]
    with open('file_path') as file_obj :
        requirements=file_obj.readlines()
       requirements= [req.replace("\n","") for req in requirements]
 
setup(
name='Machine learning project',
version='0.0.1',
author='Mg krishnan',
author_email='krishnanmg7@gmail.com',
packages=find_packages(),
install_requires=['numpy', 'pandas', 'scikit-learn', 'matplotlib', 'seaborn'],

)