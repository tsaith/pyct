# pyct
Python binding for compressive tracking.

### Packages required
- Python 3
- OpenCv3 with Python 3 support

### Build

```
python3 setup.py
```

### Run the tracker

From the webcam:

python3 run.py

From a video file with defined detecting box:

python3 run.py -v video.mp4 -b "(10, 10, 20, 20)" 

For more definitions about the arguments, 
please execute: python3 run.py -h
