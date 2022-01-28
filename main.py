import io
import numpy as np
import tensorflow as tf

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image
from typing import List

# TensorFlow Lite stuff

interpreter = tf.lite.Interpreter(model_path='static/model/model.tflite')
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

classes = ['building', 'forest', 'glacier', 'mountain', 'sea', 'street']

def predict(image):
    # [1 150 150 3]
    input_shape = input_details[0]['shape']
    input_data = tf.keras.utils.img_to_array(image).reshape(input_shape)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index']).reshape(6, )
    return classes[np.argmax(output_data)]


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def main():
    files = ['Building.jpg', 'Forest.jpg', 'Glacier.jpg', 'Mountain.jpg', 'Sea.jpg', 'Street.jpg']

    paths = ['static/images/' + x for x in files]

    classes_list = ['Building', 'Forest', 'Glacier', 'Mountain', 'Sea', 'Street']

    empty_column_labels = []

    content = html_open_tag + head_tag + body_center_open_tag + marquee_tag + heading + table_tag(paths, classes_list,
                                                                                                  empty_column_labels) + form_tag + body_center_close_tag + html_close_tag

    return content


@app.post("/predictions/", response_class=HTMLResponse)
async def get_predictions(files: List[UploadFile] = File(...)):
    
    pillow_images = []
    predictions = []
    new_size = (150, 150)
    
    for file in files:
        f = await file.read()
        img = Image.open(io.BytesIO(f)).resize(new_size)
        pillow_images.append(img)
        predicted_class = predict(img)
        predictions.append(predicted_class)


    names = [file.filename for file in files]

    for image, name in zip(pillow_images, names):
        image.save('static/' + name)

    image_paths = ['static/' + name for name in names]

    column_labels = ["Image", "Prediction"]


    return html_open_tag + table_tag(image_paths, predictions, column_labels) + html_close_tag


# Static tags

html_open_tag = """<html>"""

head_tag = """<head><meta name="viewport" content="width=device-width, initial-scale=1"/></head>"""

body_center_open_tag = """<body><center>"""

marquee_tag = """<marquee width="680" behavior="scroll"><h1 style="color:blue;font-family:Arial">Please upload your 
scenes</h1></marquee> """

heading = """<h3 style="font-family:Arial">The application will try to predict which of these categories they 
are:</h3> """

form_tag = """
            <form action="/predictions/" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple>
                <input type="submit" value="Predict!">
            </form>
           """

body_center_close_tag = """</center></body>"""

html_close_tag = """</html>"""


# Dynamic tag
def table_tag(image_paths, classes, column_labels):
    s = '<table align="center">'

    if column_labels:
        s += '<tr><th><h4 style="font-family:Arial">' + column_labels[
            0] + '</h4></th> <th><h4 style="font-family:Arial">' + column_labels[1] + '</h4></th></tr>'

    for name, image_path in zip(classes, image_paths):
        s += '<tr><td><img height="80" src="/' + image_path + '" ></td>'
        s += '<td style="text-align:center">' + name + '</td></tr>'

    s += '</table>'

    return s
