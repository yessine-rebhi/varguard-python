from setuptools import setup, find_packages

setup(
    name='varsguard',
    version='0.0.12',
    description='Python wrapper for the VarsGuard CLI tool.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Yessin Rebhi',
    author_email='rabhiyassin@gmail.com',
    url='https://github.com/yessine-rebhi/varsguard-python',
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
            'varsguard-python=varsguard.cli:VarsGuard'
        ]
    },
)