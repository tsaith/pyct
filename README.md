# pyct
A python binding for [compressive tracking](http://www4.comp.polyu.edu.hk/~cslzhang/CT/CT.htm) which is designed for real-time object tracking. 

### Demo
- Kitesurf: https://youtu.be/7fYTloE1KCc 
- Bolt: https://youtu.be/XeH4oDwVZj8

### Packages required
- python 3
- opencv 3 with python 3 support
- numpy
- cython

### Build
Following command will build the python binding for the c++ version of compressive tracking.
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

### Remark

There is also a [post](http://tsaith.github.io/blog/2015/09/30/a-python-binding-of-compressive-tracking/) describing some details about this binding.

