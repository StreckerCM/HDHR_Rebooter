# HDHomeRunRebooter
HDHomeRun Rebooter is a python script that uses the command line tools to get a list of all the HDHomeRun devices on the network and send a restart request

#prerequisites

##Operating System

Tested on Ubuntu Linux but it should work on most other flavors.  It may also work on Apple MacOS, but you will have to change the script to point at the correct hdhomerun_config location

##Python

Known compatability with: Python 2

See Python Software Foundation website for details (https://www.python.org/downloads/)

##hdhomerun_config

See the SiliconDust support page for Linux for details (https://www.silicondust.com/support/linux/)

#installation

## 1. getting the code

You can either just download it as a [zip file](https://github.com/StreckerCM/HDHR_Rebooter/archive/master.zip) and unzip it on your server, or you can use git to clone it ( git clone https://github.com/StreckerCM/HDHR_Rebooter.git ). The main benefit with git clone is that you can update to latest version very easily.

## 2. Make it executable

sudo chmod +x HDHR_Reboot

#running it

simple application just type
./HDHR_Reboot

#TL;DR
```
wget https://raw.githubusercontent.com/StreckerCM/HDHR_Rebooter/master/HDHR_Reboot
sudo chmod +x HDHR_Reboot
./HDHR_Reboot
```

#FAQ

##Why is this section devoid of questions?

Ask me a question and find out
