from setuptools import find_packages , setup 
from typing import List 


# Taking the filename in str format and returning the list of data
def get_requirements(filename : str ) -> List[str] :

    HYPHON_E = 'e.'

    with open(filename) as file :
        data = file.readlines()
        requirements = [i.replace('\n' , '') for i in data ]

        if HYPHON_E in requirements :
            requirements.remove(HYPHON_E)

    return requirements

setup (
    name = "Regression Project" ,
    version = '1.0.0',
    author = 'Mahendra_Patil',
    author_email = "gharadpatil75@gmail.com",
    install_requires = get_requirements("requirements.txt"),
    packages = find_packages()

)