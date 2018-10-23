from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"Honey Bottle,honey,honey squeeze","limit":111,"chromedriver":"C:\\Drivers\\chromedriver\\chromedriver.exe","print_urls":True}   #creating list of arguments
#Make sure to set chromedrive is the appropriate director if you want to download more than 100 images
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
