## Image quality decreaser

### To start the app execute these steps
##### Create virtual environment 
###### virtualenv venv or python3 -m venv venv

### Activate virtual environment
###### . venv/bin/activate

### Install req
###### python -m pip install -r requirements.txt

### To start redis execute
###### docker run -d -p 6379:6379 redis

### To start celery execute
###### celery -A src.config.celery_app:celery_app  worker --loglevel=info


### To start app 
###### uvicorn src.main:app --reload



###### /upload is an endpoint for uploading images which returns image_id nad task_id
###### /results is an endpoint where you can access image in decreased quality. Quality you can choose
###### I made quality to be chosen as parameter, not as nested parameters  e.g. (?quality=100/75/50/25), like was proposed in the task