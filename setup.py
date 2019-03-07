from setuptools import setup

VERSION = '0.0.3'

description = (
    'Include common chatbot functionality.'
)

install_requires = ['requests']

packages = [
    'skore',
    'skore.meya'
]

setup(
    name='skore-chatbot-sdk',
    version=VERSION,
    description=description,
    url='https://github.com/skore-io/skore-chatbot-sdk',
    author='skore.io',
    author_email='support@skore.io',
    license='None',
    packages=packages,
    install_requires=install_requires,
    zip_safe=False)
