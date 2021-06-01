from setuptools import setup, find_packages

setup(
    name="ml_benchmarks",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
    ],
)