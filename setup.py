from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:

    requirements_list: List[str] = []

    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:

                requirements = line.strip()
                if requirements and requirements != '-e .':
                    requirements_list.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found. No requirements will be added.")

    return requirements_list
print(get_requirements())
setup(
    name='AI_Trip_Planner',
    version='0.0.1',
    author='Ajay Kumar',
    author_email="burraajaykumar04@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    description='AI Trip Planner is a web application that helps users plan their trips using AI.'
)
