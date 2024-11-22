from setuptools import setup, find_namespace_packages

setup(
    name='MLatom2ase',
    version='0.0.1',
    author='Kang mingi',
    author_email='kangmg@korea.ac.kr',
    description='MLatom Calculator for ASE Interface',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  
    url='https://github.com/kangmg/MLatom2ase',
    #include_package_data=True,
    packages=find_namespace_packages(), 
    install_requires=[
        'ase',
        'mlatom'
        # 'dft4' # via conda
    ],
    classifiers=[ 
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Chemistry'
    ],
)
