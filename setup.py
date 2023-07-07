import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydoda",
    version="1.0.3",
    author="Saad Outchakoucht",
    author_email="outsaad03@gmail.com",
    description="A wrapper Python library for working with the DODa dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saad-out/pydoda",
    packages=setuptools.find_packages(),
    install_requires=[
        "pandas",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    include_package_data=True,
    package_data={
        "pydoda": [
            "dataset/*",
            "dataset/images/*",
            "dataset/semantic categories/*",
            "dataset/syntactic categories/*",
            "dataset/x-tra/*",
        ]
    },
    python_requires=">=3.6",
)
