import os
from setuptools import setup, find_packages


def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''


setup(
    name='raimon49.norilog',
    version='1.0.0',
    description='The NoriLog web application.',
    long_description=read_file('README.rst'),
    long_description_content_type='text/x-rst',
    author='raimon49',
    author_email='raimon49@hotmail.com',
    url='https://github.com/raimon49/pypro3-ch02-ch03',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Flask',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    keywords=['web', 'norilog'],
    license='BSD License',
    install_requires=[
        'Flask',
    ],
    entry_points="""
        [console_scripts]
        norilog = norilog:main
    """,
)
