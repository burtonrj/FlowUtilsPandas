from setuptools import setup, Extension
try:
    from numpy import get_include
except ImportError:
    raise RuntimeError(
        "NumPy is required to build the C extension in FlowUtils")


logicle_extension = Extension(
    'flowutilspd.logicle_c',
    sources=[
        'flowutilspd/logicle_c_ext/_logicle.c',
        'flowutilspd/logicle_c_ext/logicle.c'
    ],
    include_dirs=[get_include(), 'flowutilspd/logicle_c_ext'],
    extra_compile_args=['-std=c99']
)

setup(
    name='FlowUtilsPandas',
    version='0.1.0',
    packages=['flowutilspd'],
    package_data={'': []},
    description='Flow Cytometry Standard Utilities',
    license='BSD',
    ext_modules=[logicle_extension],
    install_requires=['numpy>=1.7', 'pandas>=0.2']
)
