from python:3.7-alpine
workdir /app
env FLASK_APP=app.py
env FLASK_RUN_HOST=0.0.0.0
run apk add --no-cache gcc musl-dev linux-headers
run apk add --no-cache build-base
copy requirements.txt requirements.txt
copy app.py app.py
copy templates ./templates
copy static ./static
copy dump ./dump
run pip install -r requirements.txt
expose 5000
expose 3306
cmd ["python3", "app.py"]
