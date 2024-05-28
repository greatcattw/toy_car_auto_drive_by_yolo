# install OS
install U22 by SD card  
require my password to logi in  
<br>
# install GPU driver  
--firstboot  
sudo apt-get update  
sudo apt-get -y install build-essential  
reboot  
<br>
--login UI  
ctrl+alt +F3  
sudo /etc/init.d/gdm3 stop  
<br>
sudo ./NVIDIA-Linux-x86_64-550.40.07.run  
[Continue installation]  
disabled Nouveau kernel [OK]  
configuration files for you? [Yes]  
/etc/modprobe.d/nvidia-installer-disable-nouveau.conf [OK]  
[Continue installation]  
-- Building kernel modules ...  
32-bit compatibility libraries? [Yes]  
[OK]  
[Rebuild initramfs]  
Any pre-existing X configuration file will be backed up. [No]  
now complite. [OK]  
[OK]  
<br>
reboot  
<br>
## verify
nvidia-smi  
<br>
# install cudnn
sudo dpkg -i cudnn-local-repo-ubuntu2204-9.1.1_1.0-1_amd64.deb  
sudo cp /var/cudnn-local-repo-ubuntu2204-9.1.1/cudnn-*-keyring.gpg /usr/share/keyrings/  
sudo apt-get update  
sudo apt-get -y install cudnn-cuda-12  
<br>
# install Anaconda
sh Anaconda3-2024.02-1-Linux-x86_64.sh  
enter  
spacex74  
yes  
--/home/xxx/anaconda3  
[Enter]  
--SHELL  
yes  
<br>
## verify
new terminal,  
(base)  
<br>
# install py lib for yolo  
pip ultralytics  
<br>
## verify
python yolov8_pred_test.py
