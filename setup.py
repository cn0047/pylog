import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='realtimelog',
    version='1.1.1',
    author='V. Kovpak',
    author_email='cn007b@gmail.com',
    description='Python package for REAL-TIME log, see: https://github.com/cn007b/log, https://realtimelog.herokuapp.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cn007b/pylog',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
