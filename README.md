# Awesome Toy Classifier

TensorFlow | Keras | FastAPI | Heroku | CNN

Hereby I am going to show a simple example that includes the most important steps in the lifecycle of a Machine Learning project. Do I skip any fine grained steps? Yes, of course! And that is because my purpose is to show an example that can be shareable in a LinkedIn post. 

The application deployed in *[Heroku](https://awesome-classifier.herokuapp.com/)* available for final users is the outcome of the following steps:

- Data Preprocessing
- Model development
- Model training
- Model evaluation
- Model Deployment  



## The dataset: 

I am going to use the so called `Intel Image Classification`. I do not know certainly whether comes from Intel or not. However, It is widely named like that in Kaggle and other sources.  

Some facts about the dataset:

- It contains 6 classes: building, forest, glacier, mountain, sea and street.
- Each element within this dataset is an image of 150px x 150px
- There are 3 folders: test, validation and training. test folder contain 7300 images that can be used for testing the model with new data. training folder and validation folder are used during **model training** step.
