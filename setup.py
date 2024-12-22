from setuptools import setup, find_packages

setup(
    name='varguard-python',
    version='0.0.10',
    description='Python wrapper for the VarGuard CLI tool.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Yessin Rebhi',
    author_email='rabhiyassin@gmail.com',
    url='https://github.com/yessine-rebhi/varguard-python',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'varguard-python=varguard.cli:VarGuard'
        ]
    },
)