# How to run YoloV3 the Easy Way, using Pytorch on Windows



## Step 1 - Requirements

* Anaconda – Python 3.6 (Win 10) 
  https://www.anaconda.com/download/

* Conda Env – Yolo.yml

🔗 https://github.com/reigngt09/yolov3workflow/tree/master/2_YoloV3_Execute

  ```conda env create -f D:\4K\yolo\RAW\Yolov3\2.YoloV3\yolo.yml```

* CUDA Toolkit - V9.0  (Nvidia GPU – GTX 1050 or higher)
  CUDA and CuDNN can now be installed via Anaconda, but if you choose to install them using the ol skool method then follow the links below.

	🔗 https://developer.nvidia.com/cuda-90-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal 

* CuDNN - V 7.05 

	🔗 https://developer.nvidia.com/rdp/cudnn-archive

  Add the following paths to Environmental Variables
    * C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\bin.
  
    * C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\include.
    
    * C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\lib\x64.
    
## Step 2 - PyTorch Yolo v3
Change directory to a workplace where you want to download the repo                                                                                                                                                                                                     

  * Clone Yolo v3 Repo
  
	  * ```git clone https://github.com/ayooshkathuria/pytorch-yolo-v3.git```

  * Download the Weights
  
  	🔗https://pjreddie.com/media/files/yolov3.weights

## Step 3 - PyTorch Yolo v3

