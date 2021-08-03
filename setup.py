import re
from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('eporner/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)[1]

with open('README.md') as f:
    readme = f.read()

setup(
    name='eporner.py',
    author='boobfuck',
    url='https://github.com/boobfuck/eporner.py',
    project_urls={
        'Documentation': 'https://epornerpy.readthedocs.io/en/latest',
        'Issue tracker': 'https://github.com/boobfuck/eporner.py/issues'
    },
    version=version,
    packages=['eporner'],
    license='MIT',
    description='A simple asynchronous Eporner API wrapper.',
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.7.0'
)
