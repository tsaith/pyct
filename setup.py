from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np

setup(ext_modules = cythonize(Extension(
           "wrap", # the extesion name
           sources=["wrap.pyx", "compressive_tracker.cpp"],  # the source files
           language="c++",                       # generate and compile C++ code
           include_dirs=[np.get_include(), "/usr/local/opt/opencv3/include"], # please check the OpenCv include path
           library_dirs=["/usr/local/opt/opencv3/lib"], # plase check the OpenCv lib path
           libraries=["opencv_core", "opencv_imgproc", "opencv_highgui", "opencv_videoio"],
      )))

