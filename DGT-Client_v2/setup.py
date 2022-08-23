from setuptools import setup
from setuptools import find_packages
setup=(
        name="BGT Client"
        version='1.0.0'
        description = "This package provides a client for the BGT transaction family"
        author = "Misha Khvatov"
        author_email = "misha.khvatov@gmail.com"
        url="https://github.com/Mishark-dev/DGT-Client"
        entry_points={'console_scripts' :
            [
                "bgtc = client.main:main"
                ]
            }
        packages=find_packages(),
        dependencies=['requests','ipaddress','cbor',
                      'protobuf==3.20','openssl','configparser']

        )
