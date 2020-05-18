from setuptools import find_packages, setup

setup(
    name='todoapp',
    version='1.0.4',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'package': ['./app.py'],
    },
    zip_safe=False,
    install_requires=[
        'flask',
        'mongoengine',
        'flask_cors',
        'waitress',
        'Flask-Cors'
    ],
)