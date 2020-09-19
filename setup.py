import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tplinkrouter-menahishayan",
    version="0.1.0",
    author="Menahi Shayan",
    author_email="menahi.shayan@gmail.com",
    description="TP-Link Archer C50 API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/menahishayan/TP-Link-Archer-C50-API",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)