**Create environment for TensorFlow**
python -m venv .tf-env

**Activate the environment**
source .tf-env/bin/activate

**Install some dependencies**
pip install --upgrade pip
pip install tensorflow==2.6.0
pip install --upgrade keras==2.6.0

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

**Some Heroku commands for troubleshooting**
heroku plugins:install heroku-builds
heroku logs --tail -a awesome-classifier
heroku run ls -R -a awesome-classifier