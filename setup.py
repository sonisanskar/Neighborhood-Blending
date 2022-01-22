from setuptools import setup

exec(open('src/version.py').read())
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name='NeighborBlend',
	version=__version__,
	decription='Iterative Weighted average of the neighbors',
	py_modules=['NeighborBlend'],
	package_dir={'':'src'},
	license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",

        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],

    install_requires=[
   'numpy',
   'pandas',
    'faiss-cpu',
    'scikit-learn'
   
],
    python_requires='>=3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Soni Sanskar",
    author_email="soni.sanskar@gmail.com",
    url="https://github.com/sonisanskar/Neighborhood-Blending",
    packages=['faiss']
    
)