from libcpp.vector cimport vector

ctypedef unsigned char uint8

cdef extern from "compressive_tracker.h":
    cdef cppclass CompressiveTracker:
        CompressiveTracker() except +
        void init_wrap(vector[vector[uint8]] &_frame, vector[int] &_objectBox)
        void process_frame_wrap(vector[vector[uint8]] &_frame, vector[int] &_objectBox)

cdef extern from "opencv2/core/core.hpp" namespace "cv":
    cdef cppclass CvRect "cv::Rect":
        Rect() except +
        Rect(int x, int y, int width, int height) except +
        int x
        int y
        int width
        int height


cdef class CyCompressiveTracker:
    cdef CompressiveTracker *this_ptr

cdef class Rect:
    cdef CvRect *this_ptr

