from setuptools import setup

<<<<<<< HEAD
VERSION = '0.0.3'
=======
VERSION = '0.0.5'
>>>>>>> develop

description = (
    'Include common chatbot functionality.'
)

install_requires = ['requests', 'meya']

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
