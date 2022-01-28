import tensorflow as tf

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def main():

    files = ['Building.jpg', 'Forest.jpg', 'Glacier.jpg', 'Mountain.jpg', 'Sea.jpg', 'Street.jpg']

    paths = ['static/images/' + x for x in files]

    classes_list = ['Building', 'Forest', 'Glacier', 'Mountain', 'Sea', 'Street']

    empty_column_labels = []

    content = head_tag + body_open_tag + marquee_tag + heading + table_tag(paths, classes_list, empty_column_labels) + form_tag + body_close_tag
    
    return content


#Static tags
head_tag = """<head><meta name="viewport" content="width=device-width, initial-scale=1"/></head>"""

body_open_tag = """<body><center>"""

marquee_tag = """<marquee width="680" behavior="scroll"><h1 style="color:blue;font-family:Arial">Please upload your scenes</h1></marquee>"""

heading = """<h3 style="font-family:Arial">The application will try to predict which of these categories they are:</h3>"""

form_tag = """
            <form  action="/uploadfiles/" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple="multiple">
                <input type="submit" value="Predict!">
            </form>
           """

body_close_tag = """</center></body>"""

# Dynamic tag
def table_tag(image_paths, classes, column_labels):
    s = '<table align="center">'
    
    if column_labels:
        s += '<tr><th><h4 style="font-family:Arial">' + column_labels[0] + '</h4></th> <th><h4 style="font-family:Arial">' + column_labels[1] + '</h4></th></tr>'
    
    for name, image_path in zip(classes, image_paths):
        s += '<tr><td><img height="80" src="/' + image_path + '" ></td>'
        s += '<td style="text-align:center">' + name + '</td></tr>'
    
    s += '</table>'
    
    return s