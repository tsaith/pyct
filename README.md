# pyct
Python binding for compressive tracking.

### Packages required
- python 3
- openCv 3 with python 3 support
- numpy
- cython

### Build
Following command will build the python binding (named `wrap.so`) for the lib of compressive tracking written in c++.
```
python3 setup.py
```
### Run the tracker

From the webcam:
```
python3 run.py
```

From a video file with the detecting box specified:
```
python3 run.py -v video.mp4 -b "(10, 10, 20, 20)" 
```

For more definitions about the arguments, please execute 
```
python3 run.py -h
```
