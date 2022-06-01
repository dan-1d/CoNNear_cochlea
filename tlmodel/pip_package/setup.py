#from distutils.core import setup, Extension
#from distutils.core import Extension
from setuptools import setup, Extension

# module1 = Extension('coclea_utils',
#                     sources = ['src/cochlea_tl_model/cochlea_utils.c'])

# setup (name = 'cochlea-tl-model-dan-1d',
#        version = '0.0.1',
#        description = 'This is a demo package',
#        ext_modules = [module1])


setup_args = dict(
    ext_modules = [
        # CTypes(
        #     'cochlea_utils',
        #     sources = ['src/cochlea_tl_model/cochlea_utils.c'],
        #     # include_dirs = ['lib'],
        #     py_limited_api = True
        # )
        Extension(
            'cochlea_utils',
            sources = ['src/cochlea_tl_model/cochlea_utils.c'],
            extra_compile_args = ["-fpic", "-O3", "-ffast-math"],
            # include_dirs = ['lib'],
            # py_limited_api = True
            language="C"
        )
    ]
)
setup(**setup_args)