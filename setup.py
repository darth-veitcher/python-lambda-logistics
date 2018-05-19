from setuptools import setup
import os
import pypandoc

import pylambd.__about__ as about


current_dir = os.path.abspath(os.path.dirname(__file__))

try:
    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace("\r", "")  # YOU  NEED THIS LINE
except OSError:
    print("Pandoc not found. Long_description conversion failure.")
    import io

    # pandoc is not installed, fallback to using raw contents
    with io.open('README.md', encoding="utf-8") as f:
        long_description = f.read()

setup(
    name='Python Lambda Logistics',
    version=about.__version__,
    url='https://github.com/darth-veitcher/python-lambda-logistics',
    license='MIT',
    author='James Veitch',
    author_email='james@jamesveitch.com',
    description=about.__description__,
    long_description=long_description if long_description else None,
    packages=['python-0lambda-logistics'],
    zip_safe=False,
    install_requires=[

    ],
    include_package_data=True,
    platforms='any',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='python lambda local docker deploy compile',
    python_requires='>=3.6',
)