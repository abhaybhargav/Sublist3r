from setuptools import setup

install_dependencies = (
    'requests == 2.8.14',
    'dnspython == 1.15.0',
    'argparse == 1.4.0'
)

setup(
    name='New_Sublist3r',
    version='',
    packages=['','subbrute'],
    package_dir={'': 'New_Sublist3r'},
    package_data={'subbrute':['*']},
    url='',
    license='',
    author='',
    install_requires = ['requests','dnspython','argparse', 'pyyaml', 'termcolor'],
    author_email='',
    description=''
)
