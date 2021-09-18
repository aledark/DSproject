from python:3.8
workdir /app
env FLASK_APP=app.py
env FLASK_RUN_HOST=0.0.0.0
copy requirements.txt requirements.txt
copy app.py app.py
copy templates ./templates
copy static ./static
copy db ./db
run pip install -r requirements.txt
expose 5000
cmd ["python3", "app.py"]
