from setuptools import setup

scripts = ['encryptfn.py']
with open('README.md', 'r') as f:
    long_description = f.read()
setup(
    name='encryptfn',
    version='0.1.0a',
    packages=['encryptfn'],
    scripts=scripts,
    url='https://github.com/btrspg/encrypt-filenames',
    license='MIT',
    author='CHEN Yuelong',
    author_email='yuelong.chen.btr@gmail.com',
    description='encrypt filenames so that others could not find any information from the filenames',
    long_description=long_description
)
