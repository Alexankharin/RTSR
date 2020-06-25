# RTSR
Real-time superresolution

Thanks to https://github.com/krasserm/super-resolution , whose code was used during development!

Here is the script for real-time superresolution ising RTSR convolutional network
Requirements 


You need a video card with support for cuda and cudnn (https://developer.nvidia.com/cuda-gpus) and the installed cuda / cudnn libraries. You need installed ptyhon 3.7 and tensorflow (version higher than 2.0 with gpu support). This can be a daunting task, and compatibility issues (https://www.tensorflow.org/install/source_windows) may occur. The easiest way would be to install the Anaconda distribution (https://www.anaconda.com/products/individual), and then open Anaconda Prompt command line and write


conda install tensorflow-gpu


If it doesn’t work out due to conflicts, then


conda install cudnn


pip install tensorflow-gpu


should work.


Other libraries can be installed using pip:
pip install opencv-python
pip install h5py

Linux only:
pip install mss
Windows only:


pip install d3dshot


After start script will show 640x480 capture region. Use WSAD keys to adjast capture position and IJKL keys for capture region size change. Key Q closes the program. Key 0 starts superresolution mode. Keys 1-2 change capture parameters ( 2 is deafalt mode for most of DOS games (see https://www.dosgamers.com/dos/dosbox-dos-emulator/screen-resolution), 1 is full pixel mode)
