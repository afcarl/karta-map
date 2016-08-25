from setuptools import setup, find_packages

setup(
        name='mapping',
        version='0.0a2',
        packages=find_packages(),
        author="Nat Wilson",
        description="Mapping utilities for karta",
        install_requires=['numpy>=1.7',
                          'scipy>=0.12',
                          'karta>=0.5.0',
                          'matplotlib>=1.5',
                          'typing'],
        license = "MIT License",
      )


