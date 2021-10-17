# Multi-label-classification

## Team members
* Tran Cong Thinh
* Nguyen Hoang Phuc
* Chau Hoang Tu
* Vu Thi Quynh Nga

## 2 stages of our solution:
1. Preprocessing the input data
2. building the model

## 1. First stage

Step 1: Resize the images into the size of 128x128

Step 2: Enhance the images' quality by using a trained autoencoder model

![image](https://user-images.githubusercontent.com/68393604/137612249-01147c53-0957-4bc1-8686-679dd0182b76.png)

![image](https://user-images.githubusercontent.com/68393604/137612243-a66e42f5-46db-46ea-a0ad-b93507df1762.png)

Step 3: Augment images by using Albumentations’ s functions
After using an autoencoder model, we saw an increase in 2 percent in the test accuracy (from 96 → more than 98)

Step 3: Augment images by using Albumentations’ s functions 
We used 5 below Albumentations’ s functions to augment our image dataset
* OpticalDistortion
* ColorJitter
* Rotate
* RandomShadow
* Cutout

Step 4: Convert labels to fit with the multi-label model

Because there are ***7 unique labels*** according to the given json file, and a maximum of ***5 different attributes*** in one image, we decide to convert the labels in a special way to fit with the multi-label model.

* The 7 unique labels : “straight” , ”left”, “right”, “entrance to the ring”, “slightly to the left”, “slightly on the right”, “to the right followed by the left turn”.
* The 5 attributes representing for the maximum of 5 lanes in an image.

![image](https://user-images.githubusercontent.com/68393604/137613928-7860b45b-f90f-48c9-95ea-8088eecd7af1.png)

As you can see on the screen, this is a ***5x7 matrix*** representing the label “left, right+straight” on the dataset. Since the maximum of attributes/lanes in an image is 5, there are 5 rows in this matrix. Similarly, as there are 7 types of basic attributes in the json file, this matrix also has 7 columns. 

After that, we flatten the matrix to fix it in our multi-label model.

![image](https://user-images.githubusercontent.com/68393604/137613934-3e235c0c-2063-448e-8665-efcdfa9d972d.png)


## 2. Second stage

In the second stage of the solution, we train our multi-label model. Below is the *structure* of our best model so far. 

![image](https://user-images.githubusercontent.com/68393604/137613817-4aba8cd5-4a5d-4592-a515-a68cd477802e.png)

Attention to our output layer, which has ***35 nodes*** and ***a sigmoid activation***, not softmax. 

After many trials-and-errors, we choose to use the ***ROC-AUC score*** since the normal accuracy metrics did not work well in this case. We also use ***binary cross-entropy*** loss to train this model. 


## 3. Deployment

Link the web deployment: [Web deployment](https://youtu.be/bgvxYvRIEf0) <br>
We have used Flask in order to deploy the model and W3CSS to style the web appearance. We also have made the web responsive to any changes so this appearance will be perfect on every type of screen.

## 4. Model's strengths

Using the labels’ converted 5x7 matrix, we can label the directions of traffic on the lanes from left to right, and easily distinguish the combinated attribute (for example,left+straight) of the image.

Compared to the normal classification model (which takes the whole label as a new class). Our model is:

***Able to break the labels into its most basic parts while still retaining its spatial information***: For instance, we don’t take “left, right+straight” as one single, seperate class. Rather, we divide them into “left” on the first attribute, “straight” and “right” on the second attribute. 

→ Be more ***flexible in practical situations:*** Since in reality, the model may encounter a sign that it hasn’t been trained on. 

***The other advantage :*** our model’s accuracy is also high on the public dataset (more than 98%), and can return the prediction results in a relatively short time. 

***Our current disadvantage:*** our model’s weight is still big → cannot publish the web online. We will try fixing this problem in the future. 

## 5. Obstacles

1. **Lack of time:** We didn’t know about the new task until three days ago. So, we have to finish our solution in a rush
2. **Low images’ quality:** the images in the new dataset the organizers provide us are in bad quality and random sizes
3. **Too many directions to try:** despite we only have 3 days to finish our project, we have many different approaches to try on (such as: ocr models, normal classification, ….), and many models to train to pick out the best one.
4. **Need many experiments to get the threshold**: we also have to submit multiple csv files with various thresholds to pick out the one that has the best accuracy on the test set.


## 6. Future vision
