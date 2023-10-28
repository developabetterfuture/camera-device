FROM python:3.11

ADD camera.py .

RUN pip install picamera

CMD ["python", "./camera.py"]