"""Setup script for run-clang-format.py"""

import setuptools


with open("README.rst", "r") as fh:
    LONG_DESCR = fh.read()

    setuptools.setup(
        name='run-clang-format',
        version='0.1',
        scripts=['run-clang-format.py'],
        author="Guillaume Papin",
        description="A wrapper script around clang-format, suitable for "
                    "linting multiple files and to use for "
                    "continuous integration",
        long_description=LONG_DESCR,
        long_description_content_type="text/x-rst",
        url="https://github.com/Sarcasm/run-clang-format",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: MIT License",
            "Operating System :: OS Independent",
        ],
    )
