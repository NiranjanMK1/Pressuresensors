from setuptools import find_packages, setup

def get_requirements():
    with open(requirement.txt) as requirement_file:
        requriement_list = requirement_file.readlines()
        requriement_list = [requirement_name.replace("\n","") for requirement_name in requriement_list]
    if "-e ." in requriement_list:
        requriement_list.remove("-e .")
        return requriement_list



setup(
    name = 'sensor',
    version= '0.0.1',
    author= 'ineuron',
    author_email = "niranjanumk@gmail.com",
    packages = find_packages()
    
    
    
    )






