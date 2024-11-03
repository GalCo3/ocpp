from setuptools import setup, find_packages

setup(
    name="ocpp",  # Keep the package name the same for compatibility
    version="1.0.0-modified",  # Use a version that reflects it's a custom version
    description="Modified version of the OCPP library from Mobility House",
    author="Your Name or Organization",
    author_email="gal.natavi@gmail.com",
    url="https://github.com/GalCo3/ocpp",
    packages=find_packages(),  # Automatically finds sub-packages
    install_requires=[
        "websockets>=9.1",  # Required for WebSocket communication
        "python-dateutil>=2.8.0",  # Commonly used for date handling
        # Add other dependencies here if known or if installation errors reveal them
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
