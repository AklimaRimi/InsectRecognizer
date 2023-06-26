# Insect Recognizer

# Motive and Goal

Rendered Website            |  
:-------------------------:|
![](https://github.com/AklimaRimi/InsectRecognizer/blob/main/output/github.png) |

As Bangladesh is an agricultural country, every year farmers lose a large amount of value due to insect attack on their crops, as a result they work hard but do not earn enough money due to spending their capital. So farmers need to know their enemies to protect their crops from insects.

In this project I wanted to create an app so that farmers can find out what pests they are facing and how to prevent those insects.

# Description

   ## ***Data Collection***
  
  I've collected data from google image. To do that I've used the `fastai` library. Go To [this](https://github.com/AklimaRimi/InsectRecognizer/blob/main/notebooks/insect_img_downloader.py) file, all the code is here. 
  As I want to recognize 13 harmful insects, about 400 images collected per insect and overall 5500 images collected for this project.

  ## ***Data Augmentation, Training and Validation***

  As I used the `fastai` api for this project, I had to do augmentation,training and validate my model at the same time. 
  1. Augmentation: resize all images and saved them as [dataloders](https://github.com/AklimaRimi/InsectRecognizer/tree/main/dataloaders)
  2. Train: For training purposes I've used the `resnet50` model. This model is faster and more accurate than any other model I found and saved them in [models](https://github.com/AklimaRimi/InsectRecognizer/tree/main/models)
  
  I've also used `resnet34`,`vgg16` which are faster but less accurate than `resnet50` 

  3. Valid: After Training I used the final trained model `model6-90%_.pkl` for validation.
  
  **Clarification**
  1. Confusion Matrix: 


  ![](https://github.com/AklimaRimi/InsectRecognizer/blob/main/output/confusion.png)
  
  2. Loss Result:


  ![](https://github.com/AklimaRimi/InsectRecognizer/blob/main/output/result.png)
  
  We can see this image is actually a `caterpillar` but the original image says it is a `Grasshopper~. So my model can correctly recognize this insect, which is a very good sign.
  
  ## ***Deployment***
  
  As I want to make an app, I have to deploy my project. So I've chosen the `HuggingFace` website to deploy. 
  
  You can find my work in here: https://huggingface.co/spaces/Rimi98/InsectRecognizer
  
  ![](https://github.com/AklimaRimi/InsectRecognizer/blob/main/output/huggingface.png)
  
  ## ***Create Interface***
  
  I created a website for this project using GitHub. The output of this website is interesting. Not only it gives the name of the insect in a image but also tells `how   could this insect could be prevented`
  
  You can find this: https://aklimarimi.github.io/InsectRecognizer/
  
  ![](https://github.com/AklimaRimi/InsectRecognizer/blob/main/output/github.png)
  
  In Gradio live(For 72 hours): https://dbad5456-2e1d-4258.gradio.live
  
# Conclusion
This project is completed, deployed and integrated. For our honourable farmers.
