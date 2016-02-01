# Geospatial assigment2: Smear Detection

First, make sure you have `Python2`, `numpy` and the Python interface of `OpenCV` installed.

Then, run `variance.py` to generate variance map for each camera.

```
python variance [path-to-cam_0-images]
python variance [path-to-cam_1-images]
...
python variance [path-to-cam_5-images]
```

And you will get `cam_[number]_vairance.npy` stores the variance map of each camera.

Last, detect smear regions by

```
python smear_det.py
```
It will plot a binary image for each npy file showing the smear and non-smear region.
