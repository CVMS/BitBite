import setuptools

with open("README.txt", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bitmeasure", # Replace with your own username
    version="0.0.1",
    author="Abhishek Kumar Chaubey",
    author_email="abhishek.chaubey@linkquestglobal.com",
    description="A Demo which demonstrate module setup",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="#",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires=['wheel'],
    python_requires='>=3.6',
)