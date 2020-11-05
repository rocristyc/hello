from setuptools import setup, find_packages

# Edit path to the auto generated versions file for your library.
# This is where the __version__ and __requires__ variables are defined
exec(open('hello/version.py').read())

setup(# make sure the 'name' here matches the one in build.gradle
      name='rocristyc-hello',
      # describe your package
      description='test python pkg for artifactory upload',
      # Boilerplate settings below.  Don't edit.
      version=__version__,
      packages=find_packages('hello'),
      package_dir={'' : 'hello'},
      install_requires=__requires__,
      )
