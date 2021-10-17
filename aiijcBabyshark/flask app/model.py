import numpy as np

import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
# from tensorflow.keras.applications import ResNet50

import json
import tensorflow.keras.backend as K
import cv2

from keras.layers import Input, Lambda
def preprocess_image(url):
    img=cv2.imread(url,1)
    img = np.expand_dims(img, axis=0)
    img=tf.image.resize(img,(128,128))
    img = img/255.
    return img



def predict(image,model):
    result = []
    predictions = model.predict(image)
    result.append(predictions)
    np_result = np.array(result).reshape(5,7)   
    return np_result

def translate_result(result):
    labels_to_use = ["straight","left","right","entrance to the ring", "slightly to the left", 
              "slightly to the right", "to the right followed by a left turn"]
    tup = np.where(result>=0.2)
    small_str=[]
    first_cl=''
    second_cl=''
    third_cl=''
    fourth_cl=''
    fifth_cl=''
    col_1 = np.where(tup[0]==0) #index column do
    col_2 = np.where(tup[0]==1)
    col_3 = np.where(tup[0]==2)
    col_4 = np.where(tup[0]==3)
    col_5 = np.where(tup[0]==4)

    if len(col_1[0])>0:
        for indice in np.array(col_1)[0]:
            first_cl = first_cl+'+'+labels_to_use[tup[1][indice]]

        first_cl=first_cl[1:]+','

    if len(col_2[0])>0:
        for indice in np.array(col_2)[0]:
            second_cl = second_cl+'+'+labels_to_use[tup[1][indice]]

        second_cl=second_cl[1:]+','

    if len(col_3[0])>0:
        for indice in np.array(col_3)[0]:
            third_cl = third_cl+'+'+labels_to_use[tup[1][indice]]

        third_cl = third_cl[1:]+','

    if len(col_4[0])>0:
        for indice in np.array(col_4)[0]:
            fourth_cl = fourth_cl+'+'+labels_to_use[tup[1][indice]]

        fourth_cl = fourth_cl[1:]+','

    if len(col_5[0])>0:
        for indice in np.array(col_5)[0]:
            fifth_cl = fifth_cl+'+'+labels_to_use[tup[1][indice]]

        fifth_cl = fifth_cl[1:]+','
    final_str= first_cl+second_cl+third_cl+fourth_cl+fifth_cl
    return final_str

def load_model(path):
    model = tf.keras.models.load_model(path, compile=False)
    # model.make_predict_function()
    return model

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

def top(scores,class_names, n=5):
    top_scores=[]
    top_scores_percentage=[]
    for i in range(n):
        top_scores.append(class_names[np.argmax(scores)])
        top_scores_percentage.append(str(100*np.max(scores)))
        scores = np.delete(scores, np.argmax(scores))
        class_names = np.delete(class_names,np.argmax(scores))

    return top_scores, top_scores_percentage

def rescale_img(img): #return a [0-255] image
  new_arr = ((img - img.min()) * (1/(img.max() - img.min()) * 255)).astype('uint8')
  img_new = np.zeros(shape=(80,80,3), dtype= np.int16)
  img_new[..., 0] = new_arr[...,2]
  img_new[...,1]=new_arr[...,1]
  img_new[..., 2] = new_arr[...,0]
  return img_new
