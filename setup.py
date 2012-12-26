from distutils.core import setup

setup(
	name='irlib',
	version='0.1.0',
	author='Tarek Amr',
	author_email='',
    url='https://github.com/gr33ndata/irlib',
	packages=['irlib'],
	license='LICENSE.txt',
	description='Inforamtion Retrieval Library',
	long_description=open('README.rst').read(),
    install_requires=["setuptools"],
)