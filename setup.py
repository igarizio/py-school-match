import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='py-school-match',
    version='0.2.0',
    packages=find_packages(exclude=('tests', 'tests.*')),
    url='https://github.com/igarizio/py-school-match',
    license='GLP v3',
    author='Iacopo Garizio',
    author_email='info@iacopogarizio.com',
    description='Py-school-match, a Python package that implements matching algorithms for the student-to-school assignation problem.',
    long_description=read('README.rst')
)
