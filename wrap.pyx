import cython
import numpy as np
cimport numpy as np
from libcpp.vector cimport vector

cimport wrap

cdef class CyCompressiveTracker:
    def __cinit__(self, frame, object_box):
        self.this_ptr = new CompressiveTracker()

        cdef vector[int] c_object_box
        c_object_box.push_back(object_box.x)
        c_object_box.push_back(object_box.y)
        c_object_box.push_back(object_box.width)
        c_object_box.push_back(object_box.height)

        self.this_ptr.init_wrap(frame, c_object_box)

    def __dealloc__(self):
        del self.this_ptr

    def process_frame(self, frame, object_box):

        cdef vector[int] c_object_box
        c_object_box.push_back(object_box.x)
        c_object_box.push_back(object_box.y)
        c_object_box.push_back(object_box.width)
        c_object_box.push_back(object_box.height)

        self.this_ptr.process_frame_wrap(frame, c_object_box)

        object_box.x = c_object_box[0]
        object_box.y = c_object_box[1]
        object_box.width  = c_object_box[2]
        object_box.height = c_object_box[3]

        return object_box


cdef class Rect:
    def __cinit__(self, int x, int y, int width, int height):
        self.this_ptr = new CvRect()
        self.this_ptr.x = x
        self.this_ptr.y = y
        self.this_ptr.width  = width
        self.this_ptr.height = height
    def __dealloc__(self):
        del self.this_ptr
    property x:
        def __get__(self): return self.this_ptr.x
        def __set__(self, val): self.this_ptr.x = val
    property y:
        def __get__(self): return self.this_ptr.y
        def __set__(self, val): self.this_ptr.y = val
    property width:
        def __get__(self): return self.this_ptr.width
        def __set__(self, val): self.this_ptr.width = val
    property height:
        def __get__(self): return self.this_ptr.height
        def __set__(self, val): self.this_ptr.height = val
