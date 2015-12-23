from distutils.core import setup, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

ext = Extension("cyepanet",
                sources=["lib/epanet.c", "lib/hash.c",
                         "lib/rules.c", "lib/hydraul.c", "lib/inpfile.c",
                         "lib/input1.c", "lib/input2.c", "lib/input3.c",
                         "lib/mempool.c", "lib/output.c", "lib/quality.c",
                         "lib/report.c", "lib/smatrix.c", "cyepanet.pyx"])


setup(
        name='cyepanet',
        version='1.0',
        packages=[''],
        url='',
        license='MIT',
        author='markwilson',
        author_email='',
        description='',
        cmdclass = {'build_ext': build_ext},
        ext_modules = cythonize([ext])
)

# python setup.py build_ext --inplace