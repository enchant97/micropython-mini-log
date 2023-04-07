__version__ = "0.0.0"

from setuptools import setup


def long_description():
    with open("README.md", "r") as fo:
        return fo.read()


setup(
    name="micropython-mini-log",
    version=__version__,
    url="https://github.com/enchant97/micropython-mini-log",
    description="A MicroPython library for minimal logging",
    keywords=["micropython", "logging"],
    long_description=long_description(),
    long_description_content_type="text/markdown",
    license="Apache-2.0",
    packages=["mini_log"],
    classifiers=[
        "Private :: Do Not Upload",  # TODO remove when stable-ish
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "Topic :: System :: Logging",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: Apache Software License",
    ],
)
