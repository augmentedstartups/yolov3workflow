
# Supervisely Cluster Setup

## Introduction
Hey guys and welcome back, so in this lecture, we are going to setup up our deep learning capable PC as a cluster for Supervisely. Now we are using Ubuntu because it is required by Supervisely, otherwise we would be using windows. But what is nice about this setup is that you can access this PC anywhere in the world and train your CNN models from the otherside of the planet if you really wanted to. Ideally you would want your cluster to be a server rather than your desktop PC, but hey if you have to train, you have to train. 
So my PC that I am using, has an NVidia 1080 GTX graphics card and I freshly partitioned my hard drive alongside windows. We won’t cover the installation of Ubuntu 16.04 in this series as there are tons of free tuts on how to do this. Make sure when that you Ubuntu partition has tons of space because Supervisely creates and saves weight checkpoints at every epoch which can easily consume around 20 to 30 gigs of space. I made my partition around 200Gb to allow for enough training epochs. 

The whole process of setting up a cluster is quite laborious and involves a lot of copy-and-pasting of command lines but once you set it up, its done for good, unless you ran out of space like I did and had to set it up twice on two computers. 
So,ya! without further A due, let’s get started with creating a Supervisely cluster:

## 1. Supervisely
Okay so first up we need to log into supervise.ly and log into our account. If you don’t have an account you can sign up.
Under the cluster tab you click here to add a node. And as you can see, they show you all the requirement to convert your PC into a cluster. This includes 
*	Linux OS with Kernal greater that 3.10, 
*	Docker version 18 and above
*	GPU with Cuda 9.0 
*	As well as a nvidia docker container with version 2.0.


## 2. Install Graphics Card Drivers
First make sure that you have your nVidia graphics card drivers installed. You can go to __Additional Drivers__ and alternative checkbox under graphics drivers.

After that is installed your Ubunutu will want to update all the drivers. 
Once that is done.

```sudo apt-get update```

Restart your PC

## 3. Install CUDA
```sudo dpkg -i cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64.deb```

```sudo apt-key add /var/cuda-repo-9-0-local/7fa2af80.pub```

```sudo apt-get update```

```sudo apt-get install cuda```

## 4. Post Cuda Installation
From 7.1.1 Environment Setup from the cuda installation guide for Linux. We put in the following commands in terminal:

https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#axzz4VZnqTJ2A

```export PATH=/usr/local/cuda-10.0/bin${PATH:+:${PATH}}```

```export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64\${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}```


## 5. Install CuDNN
Sign up for a free account to download CuDNN 9.0, Download the runtime and developer packages of cuDNN 7.0.5 for cuda 9.0.

https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html

Install CuDNN Run Time

```sudo dpkg -i libcudnn7_7.0.5.15-1+cuda9.0_amd64.deb```

Install CuDNN Dev

```sudo dpkg -i libcudnn7-dev_7.0.5.15-1+cuda9.0_amd64.deb```


## 6. Docker Installation

```sudo apt install curl```

```curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -```

Follow Docker installation process:

https://docs.docker.com/install/linux/docker-ce/ubuntu/

## 7. Post installation Steps for Linux
Follow the post installation instructions for Docker:

https://docs.docker.com/install/linux/linux-postinstall/

## 8. Nvidia Docker 2
Follow the instructions at the links below:

https://github.com/NVIDIA/nvidia-docker

or

https://nvidia.github.io/nvidia-docker/

## 9. Link to Supervisely

Copy the curl in supervisely into terminal and it should be linked!
