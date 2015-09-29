"""
Track object in video with the Compressive tracker.
"""

import cv2 # OpenCV
from wrap import CyCompressiveTracker as CompressiveTracker
from wrap import Rect
import argparse

# --------
"""
class Rect:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = x
        self.width  = width
        self.height = height
"""

def detect_box(cap, win_name):
    # Define a detection box.

    box_defined = False
    box = Rect(0, 0, 0, 0)

    def define_box(event, x, y, flags, param):

        nonlocal box_defined, box
        if event == cv2.EVENT_LBUTTONDOWN:
            box.x = x
            box.y = y
            box.width  = 0
            box.height = 0

        if event == cv2.EVENT_MOUSEMOVE:
            box.width  = x - box.x
            box.height = y - box.y

        if event == cv2.EVENT_LBUTTONUP:
            box_defined = True

    def do_nothing(event, x, y, flags, param):
        pass

    # set mouse callback
    cv2.setMouseCallback(win_name, define_box)

    while not box_defined:
        # display the frame from video capture
        _, frame = cap.read()
        clone = frame.copy()
        if box.x > 0 and box.width > 0:
            draw_rect(clone, box, (0, 255, 0), 2)
        cv2.imshow(win_name, clone)

        # This is important to activate the mouse callback
        key = wait_key(10) & 0xFF

    # Set a mouse callback which does nothing
    cv2.setMouseCallback(win_name, do_nothing)

    return box, frame


def draw_rect(image, rect, color=(0, 255, 0), thickness=2):
    # Draw a rectangle.

    # Starting and ending point of the rectangle
    p0 = (rect.x, rect.y)
    p1 = (rect.x + rect.width, rect.y + rect.height)

    cv2.rectangle(image, p0, p1, color, thickness)


def wait_key(delay):
    # Wait for a pressed key.

    return cv2.waitKey(delay) & 0xFF

def parse_box_arg(arg):
    # Parse the box argument and return a Rect object

    out = arg
    out = out.replace('(', "")
    out = out.replace(')', "")
    out = out.replace(' ', "")
    out = out.split(',')
    
    x = int(out[0])
    y = int(out[1])
    width  = int(out[2])
    height = int(out[3])

    return Rect(x, y, width, height)


# --------
# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", default=None, help="path to the video file")
ap.add_argument("-b", "--box", default=None, help="detecting box, e.g. '(10, 10, 20, 20)'")
ap.add_argument("-o", "--output", default="output.mp4", help="output video file")
args = vars(ap.parse_args())

# Arguments
video = args['video']
box = parse_box_arg(args['box']) if args['box'] else None 
output = args['output']

# Read frames form webcam or video file
if video is None:
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640);
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480);

else:
    cap = cv2.VideoCapture(video)

# In case the video can't be open
if not cap.isOpened(): 
    print("The video cann't be open!")
    exit(0)

# Creat a window
win_name = 'demo'
cv2.namedWindow(win_name)

# Read the first frame
if video is None: # When webcan is used
    # Define the detection box
    box, first_frame = detect_box(cap, win_name)
else:
    _, first_frame = cap.read()

# Initialize the compresive tracker
gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
ct = CompressiveTracker(gray, box)

# loop over the frames of the video
print("Start to track the object.")
while True:
    # grab the current frame and initialize the occupied/unoccupied
    # text
    (grabbed, frame) = cap.read()

    # if the frame could not be grabbed, then we have reached the end
    # of the video
    if not grabbed: break

    # Process the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    box = ct.process_frame(gray, box)

    # Draw the tracking box
    draw_rect(frame, box, color=(0, 255, 0), thickness=2)

    # show the frame and record if the user presses a key
    cv2.imshow(win_name, frame)

    # if the `q` key is pressed, break from the lop
    key = wait_key(1)
    if key == ord("q"): break

# Release the resources and close any open windows
cap.release()
cv2.destroyAllWindows()

