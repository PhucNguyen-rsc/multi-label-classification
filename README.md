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
     - Random brightness
     - Random Fog
     - Rotate
     - Randow shadow
     - Blur
Step 4: Convert labels to fit with the multi-label model


## 2. Second stage


## 3. Deployment


## 4. Model's strengths

## 5. Obstacles

1. **Lack of time:** We didn’t know about the new task until three days ago. So, we have to finish our solution in a rush
2. **Low images’ quality:** the images in the new dataset the organizers provide us are in bad quality and random sizes
3. **Too many directions to try:** despite we only have 3 days to finish our project, we have many different approaches to try on (such as: ocr models, normal classification, ….), and many models to train to pick out the best one.
4. **Need many experiments to get the threshold**: we also have to submit multiple csv files with various thresholds to pick out the one that has the best accuracy on the test set.


## 6. Future vision
