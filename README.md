# skore-chatbot-sdk

Include common bot functionality via custom Python packages.

# Requirements
  Python 2.7.10
  VirtualEnv

# Setup the development env
```sh
virtualenv venv
. ./venv/bin/activate
```

# Before publish the packages
```sh
pip install --upgrade pip
pip install --upgrade setuptools wheel
```

# How to public the package to pypi.org (username/password see lastpass Pypi)
```sh
python setup.py sdist bdist_wheel
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

# How to public the package to test.pypi.org
```sh
python setup.py sdist bdist_wheel
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
