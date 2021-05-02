import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='beatnik',
     version='0.1',
     #scripts=['beatnik'] ,
     author="Experimental Informatics",
     #author_email="t.liu@khm.de",
     description="A Beatnik library",
     #long_description=long_description,
     #long_description_content_type="text/markdown",
     url="https://github.com/experimental-informatics/beatnik",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )
