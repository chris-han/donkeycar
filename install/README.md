### Install on raspberry pi
The easiest way to get donkey running on a pi is with a prebuilt disk image. To create your own disk
image you can use the scripts in /pi.
or it's easier for dev to install from you git:

pip install git+https://github.com/chris-han/donkeycar
make sure you also install the dependency packages on pi since the pip extra doesn't work with git

pip install picamera

pip install Adafruit_PCA9685

You can also install Xbox One s controller following the instructions here:

https://github.com/chris-han/donkeypart_xbox_1s_controller

then create your car app - generate the drive script, config and folder structure for your car.

donkey createcar ~/mtcar


### Install on other systems
Create a conda environment using the env files in
