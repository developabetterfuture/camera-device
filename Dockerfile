FROM python:3.11

ADD camera.py .

RUN pip install picamera2

CMD ["python", "./camera.py"]