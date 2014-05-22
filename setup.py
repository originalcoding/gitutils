from distutils.core import setup

from gitutils import __doc__, __version__, __author__


P = "gitutils"


setup(
    name=P,
    description=__doc__,
    version=__version__,
    author=__author__,
    license="New BSD",
    py_modules=(P, ),
)

