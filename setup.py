from os.path import expanduser
from setuptools import setup

setup(
    name="unstar",
    version="0.0.0",
    description="Star/Unstar repositories from the command line",
    url="https://github.com/QuantumPhi/unstar",
    author="QuantumPhi",
    author_email="phi.quantum@gmail.com",
    license="MIT",
    packages=["unstar"],
    install_requires=["json", "requests"],
    zip_safe=True
)

# TODO: Client secret
"""
secret = input("Client secret: ")
f = open(expanduser("~")+"/.unstar/client_secret", "w+")
print(secret, file = f)
"""
