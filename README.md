# Insect Recognizer

# Motive and Goal

As Bangladesh is an agricultural country, every year farmers lose a large amount of value due to insect attack on their crops, as a result they work hard but do not earn enough money due to spending their capital. So farmers need to know their enemies to protect their crops from insects.

In this project I wanted to create an app so that farmers can find out what pests they are facing and how to prevent those insects.

# Description

  ## Data Collection
  
  I've collected data from google image. To do that I've used `fastbook` library. Go To [this](https://github.com/AklimaRimi/InsectRecognizer/blob/main/notebooks/insect_img_downloader.py) file, all the code is here. 
  As I want to recognize 13 harmfull insects, about 400 images collected for per insect and overall 5500 images collected for this project.
  
  ## Data Augmentation, Training and Validation
  
  As I used `fastai` api for this project, I had to do augmentation,training and valid my model at the same time. 
  1. Augmentation: resized all images and saved them as [dataloders](https://github.com/AklimaRimi/InsectRecognizer/tree/main/dataloaders)
  2. Train: For training purpose I've used `resnet34` model. This model is faster and more accurate than any other model I found and saved them in [models](https://github.com/AklimaRimi/InsectRecognizer/tree/main/models)
  3. Valid: After Training I used final trained model `model3-86_.pkl` for validation.
  
  ## Deployment
  
  As I want to make an app so I have to deploy my project. So I've choose `HuggingFace` website to deploy. 
  
  You can find my work in here: https://huggingface.co/spaces/Rimi98/InsectRecognizer
  
  It takes insects image as input and it will produce insect name and the method how to destroy them.




https://dbad5456-2e1d-4258.gradio.live
# Conclusion
