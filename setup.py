from setuptools import setup

setup(
    name="star.py",
    version="0.0.0",
    description="Star/Unstar repositories from the command line",
    url="https://github.com/QuantumPhi/unstar",
    author="QuantumPhi",
    author_email="phi.quantum@gmail.com",
    license="MIT",
    packages=["star"],
    install_requires=["json", "requests"],
    zip_safe=True
)
