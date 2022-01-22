# Awesome Toy Classifier

Hereby I am going to show a simple example that includes the most important steps in the lifecycle of a Machine Learning project. 

- Do I skip any fine grained steps? **Yes, of course!**
- Do I merge steps (1 step that includes 2 or 3 smaller steps)? **Yes, of course!** 

And this is because my purpose is to show an example that can be shareable in a LinkedIn post with its limitations.

The application deployed in *[Heroku](https://awesome-classifier.herokuapp.com/)* available for final users is the outcome of the following steps:

- Data Preprocessing
- Model Development And Training
- Prediction On New Data
- Model Deployment

## The dataset: 

I am going to use the so-called `Intel Image Classification`. I do not know certainly whether comes from Intel or not. However, It is widely named like that in Kaggle and other sources.  

Some facts about the `dataset` folder on this repository:

- It contains 6 categories: building, forest, glacier, mountain, sea and street.
- It has been slightly modified: each category contains exactly the same quantity of elements (2190 images). In the original dataset, categories are unbalanced.
- Each element within this dataset is an image of 150px x 150px
- There are 3 folders: test, validation and training. test folder contains 7300 images that can be used for testing the model with new data. training folder and validation folder are used for training the model.

## The `Image Classification` notebook

By running this notebook, I am executing the steps

- Data Preprocessing
- Model Development And Training
- Prediction On New Data

The model gets an accuracy of over than 0.9 approximately, which is perfectly acceptable for a toy classifier. I save this entire model for future usage (When the application is deployed).

## The `Upload the saved model for predicting new images` notebook

By running this notebook, I am just verifying how to load a saved model and use it for predictions.

## The `FastAPI` application

## Deployment on Heroku

## Sources:

- [Transfer learning and fine-tuning from TensorFlow](https://www.tensorflow.org/tutorials/images/transfer_learning)

-[Save and load models from TensorFlow](https://www.tensorflow.org/tutorials/keras/save_and_load)

- [Keras](https://keras.io)

- [FastAPI documentation](https://fastapi.tiangolo.com)

- [Heroku Dev Center](https://devcenter.heroku.com)