**Create environment for TensorFlow Lite**   
python -m venv .tflite-env  

**Activate the environment**   
source .tflite-env/bin/activate   

**Install some dependencies**  
pip install --upgrade pip  
pip install fastapi  
pip install uvicorn  
pip install gunicorn  
pip install tflite-runtime   
pip install pillow  
pip install python-multipart   

**Create requirements.txt file**   
pip freeze > requirements.txt  

**Start FastAPI application**  
Once the environment is active, just execute `uvicorn main:app --reload`  

**Heroku commands for troubleshooting**  

heroku login

heroku run bash -a scenes-classifier

heroku logs --tail -a scenes-classifier
