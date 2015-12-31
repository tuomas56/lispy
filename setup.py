from setuptools import setup, find_packages
setup(name="lisp", 
	package_dir={'':'src'},
	version="0.2",
	packages=find_packages('src'),
	scripts=['src/ilp'])
