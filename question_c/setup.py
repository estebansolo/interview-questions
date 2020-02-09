import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='lru_cache',
    version='0.1',
    author="Esteban Solorzano",
    author_email="estebansolorzano27@gmail.com",
    description="LRU Cache for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/estebansolo/david_solorzano_test/tree/master/question_c",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)