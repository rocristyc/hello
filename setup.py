#from setuptools import setup, find_packages
import setuptools 
with open("README.md", "r") as fh:
    long_description = fh.read()

# Edit path to the auto generated versions file for your library.
# This is where the __version__ and __requires__ variables are defined
# exec(open('rocristyc_hello/version.py').read())

setuptools.setup(# make sure the 'name' here matches the one in build.gradle
      name='rocristyc-hello',
      # describe your package
      description='test python pkg for artifactory upload',
      # Boilerplate settings below.  Don't edit.
      #version=__version__,
      version="0.0.2",
      packages=setuptools.find_packages(),      
      #packages=find_packages('rocristyc-hello'),
      #package_dir={'' : 'rocristyc-hello'},
      #install_requires=__requires__,
      )
