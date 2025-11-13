from setuptools import setup, find_packages

setup(
    name='emotagger',
    version='0.1.0',
    description='Multilingual Emotion Detection Library',
    author='Sejal Tambe',
    packages=find_packages(),
    install_requires=[
        'googletrans==4.0.0-rc1',
    ],
    entry_points={
        'console_scripts': [
            'emotagger=emotagger.__main__:main',
        ],
    },
)
