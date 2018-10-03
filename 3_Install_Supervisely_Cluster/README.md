
# Supervisely Cluster Setup

## Install Graphics Card Drivers
First make sure that you have your nVidia graphics card drivers installed. You can go to __Additional Drivers__ and alternative checkbox under graphics drivers.

After that is installed your Ubunutu will want to update all the drivers. 
Once that is done.

```sudo apt-get update```

Restart your PC

## Install CUDA
```sudo dpkg -i cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64.deb```

```sudo apt-key add /var/cuda-repo-9-0-local/7fa2af80.pub```

```sudo apt-get update```

```sudo apt-get install cuda```

## Post Cuda Installation
From 7.1.1 Environment Setup from the cuda installation guide for Linux. We put in the following commands in terminal:

https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#axzz4VZnqTJ2A

```export PATH=/usr/local/cuda-10.0/bin${PATH:+:${PATH}}```

```export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64\${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}```


## Install CuDNN
Sign up for a free account to download CuDNN 9.0, Download the runtime and developer packages of cuDNN 7.0.5 for cuda 9.0.

https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html

Install CuDNN Run Time

```sudo dpkg -i libcudnn7_7.0.5.15-1+cuda9.0_amd64.deb```

Install CuDNN Dev

```sudo dpkg -i libcudnn7-dev_7.0.5.15-1+cuda9.0_amd64.deb```


## Docker Installation

```sudo apt install curl```

```curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -```

Follow Docker installation process:

https://docs.docker.com/install/linux/docker-ce/ubuntu/

## Post installation Steps for Linux
Follow the post installation instructions for Docker:

https://docs.docker.com/install/linux/linux-postinstall/

## Nvidia Docker 2
Follow the instructions at the links below:

https://github.com/NVIDIA/nvidia-docker

or

https://nvidia.github.io/nvidia-docker/

## Link to Supervisely

Copy the curl in supervisely into terminal and it should be linked!
