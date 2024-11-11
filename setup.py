from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext
import os

ext_modules = [
    Pybind11Extension(
        "jwt_cpp",
        ["jwt_wrapper.cpp"],
        include_dirs=[os.path.join("jwt-cpp", "include"), "/opt/homebrew/include"],
        library_dirs=["/opt/homebrew/lib"],
        libraries=["ssl", "crypto"],
    ),
]
setup(
    name="jwt_cpp",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
