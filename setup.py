from setuptools import setup, find_packages

setup(
    name="ocpp",
    version="1.0.0-modified",
    description="Modified version of the OCPP library from Mobility House",
    author="Your Name or Organization",
    author_email="gal.natavi@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "ocpp.v16.schemas": ["*.json"],
    },
    install_requires=[
        "websockets>=9.1",
        "python-dateutil>=2.8.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
