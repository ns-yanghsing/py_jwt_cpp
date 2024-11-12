# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_jwt_cpp']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py_jwt_cpp',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
