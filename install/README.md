### Install on raspberry pi
The easiest way to get donkey running on a pi is with a prebuilt disk image. To create your own disk
image you can use the scripts in /pi.
or it's easier for dev to install from you git:

pip install git+https://github.com/chris-han/donkeycar.git[pi]

then create your car app - generate the drive script, config and folder structure for your car.

donkey createcar ~/mtcar


### Install on other systems
Create a conda environment using the env files in
