from setuptools import setup

setup(
    name='pointercrateCLI',
    version='0.1.0',
    description='A example Python package',
    url='https://github.com/RCNOverwatcher/PointercrateCLI',
    author='Jacob Wiltshire',
    author_email='jacobjameswiltshire@protonmail.com',
    license='MIT',
    packages=['pointercrateCLI'],
    install_requires=['requests',
                      'rich',
                      ],

    classifiers=[
        'Programming Language :: Python :: 3.11',
    ],
)
