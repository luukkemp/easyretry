from setuptools import find_packages, setup


setup(
    packages=find_packages(),
    pbr=True,
    setup_requires=['pbr'],
    version="0.9.3",
)
