from setuptools import setup

VERSION = '0.0.1'

description = (
    'Include common bot functionality via custom Python packages.'
)

install_requires = ['requests']

packages = [
    'skore',
    'skore.meya'
]

setup(
    name='pip-skore',
    version=VERSION,
    description=description,
    url='https://github.com/skore-io/pip-skore',    
    author='skore.io',
    author_email='support@skore.io',
    license='None',
    packages=packages,
    install_requires=install_requires,
    zip_safe=False)
