from python:3.8
workdir /app

copy requirements.txt requirements.txt
copy app.py app.py
copy templates ./templates
copy static ./static
copy db ./db
run pip install -r requirements.txt
expose 8000
cmd ["python3", "app.py"]
