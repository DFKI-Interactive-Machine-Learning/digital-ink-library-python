from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("LICENSE", "r") as fh:
    license_text = fh.read()

setup(
    name='digital_ink_library',
    version='1.4.1',
    packages=['digital_ink_library', 'digital_ink_library.serialization', 'digital_ink_library.conversion'],
    url='https://github.com/DFKI-Interactive-Machine-Learning/digital-ink-library-python',
    license=license_text,
    author='Alexander Prange, Michael Barz',
    author_email='alexander.prange@dfki.de; michael.barz@dfki.de',
    python_requires='>=3.6.0',
    install_requires=[
            'numpy',
            'scipy'
        ],
    description='Library for digital ink, written in Python.',
    long_description=long_description
)
