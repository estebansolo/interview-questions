import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='version_comparison',
    version='0.2',
    license="MIT",
    author="Esteban Solorzano",
    author_email="estebansolorzano27@gmail.com",
    description="Get a comparison between 2 version strings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords = ["Compare", "Versions"],
    url="https://github.com/estebansolo/david_solorzano_test/tree/master/question_b",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)