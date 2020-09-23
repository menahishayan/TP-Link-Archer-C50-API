import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tplinkrouter",
    version="0.3.3",
    author="Menahi Shayan",
    author_email="menahi.shayan@gmail.com",
    description="TP-Link Archer C50 API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/menahishayan/TP-Link-Archer-C50-API",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)