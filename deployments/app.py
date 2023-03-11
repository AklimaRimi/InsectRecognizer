import gradio as gr
from fastai.vision.all import load_learner
from fastai import *
import torch
import os
from PIL import Image
import pathlib 

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

model_path  = 'models\model3-86_.pkl'

model = load_learner(model_path)

def result(path):  
  
  pred,_,probability = model.predict(path)

  return {pred: float(probability.max())}

path = 'test_images/'

image_path = []

for i in os.listdir(path):
  image_path.append(path+i) 


image = gr.inputs.Image(shape =(128,128))
label = gr.outputs.Label()

iface = gr.Interface(fn=result, inputs=image, outputs=label, examples = image_path)
iface.launch(inline = False)
