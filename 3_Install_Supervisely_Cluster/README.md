
#CUDA installation 
sudo dpkg -i cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64.deb
sudo apt-key add /var/cuda-repo-9-0-local/7fa2af80.pub

sudo apt-get update
sudo apt-get install cuda

Post Cuda Installation
https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#axzz4VZnqTJ2A

export PATH=/usr/local/cuda-10.0/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64\
                         ${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}



https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html
Install CuDNN Run Time
sudo dpkg -i libcudnn7_7.0.5.15-1+cuda9.0_amd64.deb
Install CuDNN Dev
sudo dpkg -i libcudnn7-dev_7.0.5.15-1+cuda9.0_amd64.deb


Docker Installation
sudo apt install curl
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -




nvidia docker 2

https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0)
https://nvidia.github.io/nvidia-docker/

