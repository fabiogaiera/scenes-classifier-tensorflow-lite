# Image Classification  

Hereby I am going to show a simple example that includes the most important steps in the lifecycle of a Machine Learning project. 

- Do I skip any fine grained steps? **Yes, of course!**
- Do I merge steps (1 step that includes 2 or 3 smaller steps)? **Yes, of course!** 

And this is because my purpose is to show an example that can be shareable in a post with its known limitations.

The application deployed in *[Heroku](https://awesome-classifier.herokuapp.com/)* available for final users is the outcome of the following steps:

- Data Preprocessing
- Model Development And Training
- Prediction On New Data
- Model Deployment

## The dataset: 

I am going to use the so-called `Intel Image Classification`. I do not know certainly whether it belongs to Intel or not, however it is widely named like that in Kaggle and other sources.

Some facts about the `dataset` folder on this repository:

- It contains 6 categories: building, forest, glacier, mountain, sea and street.
- Each element within this dataset is an image of 150px x 150px
- There are 3 folders: test, validation and training. test folder contains 7300 images that can be used for testing the model with new data. training folder and validation folder are used during the model training.

## The `Model Creation` notebook

By running this notebook, I am executing the steps

- Data Preprocessing
- Model Development And Training

The model gets an accuracy of over than 0.9 approximately, which is perfectly acceptable for an example. The model is saved for future usage in two different formats: SavedModel format and TensorFlow Lite format.


## The `Model Prediction With Tensorflow` notebook

By running this notebook, I am executing the step

- Prediction On New Data

You can see how to load a model build with SavedModel format and use it for predictions.

## The `Model Prediction With Tensorflow Lite` notebook

By running this notebook, I am executing the step

- Prediction On New Data

You can see how to load a model built with TensorFlow Lite format and use it for predictions.

## The application built with `FastAPI`

Definitely FastAPI is a great framework for building web applications faster. So, I chose it for creating an app that allows you to upload and classify images within those 6 categories I mentioned before. The whole application is written in `main.py` file.

## Deployment on Heroku

Since I am using the **Free and Hobby** account, the main goal is to save space due the limitations of this account! A way of showing this MVP is to use TensorFlow Lite, which helps saving significant space when installing libraries.

## Sources:

- [Transfer learning and fine-tuning](https://www.tensorflow.org/tutorials/images/transfer_learning)

- [Image classification](https://www.tensorflow.org/tutorials/images/classification)

- [Save and load models](https://www.tensorflow.org/tutorials/keras/save_and_load)

- [TensorFlow Lite inference](https://www.tensorflow.org/lite/guide/inference)

- [FastAPI documentation](https://fastapi.tiangolo.com)

- [Heroku Dev Center](https://devcenter.heroku.com)