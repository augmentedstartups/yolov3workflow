# How to run YoloV3 the Easy Way, using Pytorch on Windows



# Step 1 - Requirements

* Anaconda – Python 3.6 (Win 10) 
  https://www.anaconda.com/download/

* Conda Env – Yolo.yml
🔗 https://github.com/reigngt09/yolov3workflow/tree/master/2_YoloV3_Execute

  ```conda env create -f D:\4K\yolo\RAW\Yolov3\2.YoloV3\yolo.yml```

* Nvidia GPU – GTX 1050 or higher


* CUDA Toolkit - V9.0 
  CUDA and CuDNN can now be installed via Anaconda, but if you choose to install them using the ol skool method then follow the links below.

🔗 https://developer.nvidia.com/cuda-90-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal 

* CuDNN - V 7.05 
🔗 https://developer.nvidia.com/rdp/cudnn-archive

  Copy the following files into the CUDA Toolkit directory.
    * Copy <installpath>\cuda\bin\cudnn64_7.dll to C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\bin.
  
    * Copy <installpath>\cuda\ include\cudnn.h to C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\include.
    
    * Copy <installpath>\cuda\lib\x64\cudnn.lib to C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\lib\x64.
    
    
