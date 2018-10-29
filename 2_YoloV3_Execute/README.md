# How to run Real-Time YoloV3 the Easy Way, using Pytorch on Windows

Hey guys and welcome back, so in this [video](http://bit.ly/YoloV3Playlist) I'm going to show you how to implement Yolo V3 Object Detection using PyTorch on Windows 10. We'll walk through everything from requirements to setup, then all the way to executing the CNN. Now we are not going to go through the theory as I mentioned earlier, this will just be hands-on practical tutorial to get you up and running. 

Just be aware that I have not been able to train YoloV3 on Windows, but this turned out to be a blessing in disguise as I now use a new workflow called Supervisely. I will show you how we can use this new workflow for annotation, to training as well as data augmentation. But for now lets get started with the execution of Yolo V3

You can find the full video series tutorial here : http://bit.ly/YoloV3Playlist

## Step 1 - Requirements

* Anaconda – Python 3.6 (Win 10) 
  https://www.anaconda.com/download/

* Conda Env – Yolo.yml

	🔗 https://github.com/reigngt09/yolov3workflow/tree/master/2_YoloV3_Execute
	
  ```cd C:\yolo```

  ```conda env create -f yolo.yml```
  
  If that does not work, try installing the dependencies with:
  
    ```pip install -r requirements.txt```
  

* CUDA Toolkit - V9.0  (Nvidia GPU – GTX 1050 or higher)
  CUDA and CuDNN can now be installed via Anaconda, but if you choose to install them using the ol skool method then follow the links below.

	🔗 https://developer.nvidia.com/cuda-90-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal 

* CuDNN - V 7.05 

	🔗 https://developer.nvidia.com/rdp/cudnn-archive
	
  * Copy the following files into the CUDA Toolkit directory.
  
   	Copy <installpath>\cuda\bin\cudnn64_7.dll to C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\bin.
	
  	Copy <installpath>\cuda\ include\cudnn.h to C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\include.
	
 	Copy <installpath>\cuda\lib\x64\cudnn.lib to C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\lib\x64.

  * Add the following paths to Environmental Variables
     C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\bin
  
     C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\include
    
     C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\lib\x64
     
  * Ensure that you have the latest nvidia graphics drivers install on your PC. You can do this from the nvidia website.
    
## Step 2 - PyTorch Yolo v3
Change directory to a workplace where you want to download the repo                                                                                                                                                                                                     

  * Clone Yolo v3 Repo
  
	  * ```git clone https://github.com/ayooshkathuria/pytorch-yolo-v3.git```

  * Download the Weights
  
  	🔗https://pjreddie.com/media/files/yolov3.weights

## Step 3 - PyTorch Yolo v3

* Change Directory to cloned repo

	 ```cd C:\yolotorch```
	 
* Download any test video (.mp4/.avi)

* Run demo on video

	 ```python video_demo.py --video video.mp4```

* Run demo on webcam

	 ```python cam_demo.py```
