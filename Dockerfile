FROM python:3.8-slim

COPY . .

WORKDIR /app
COPY app/requirements.txt ./
RUN pip install -r requirements.txt 


RUN pip install Django
RUN pip install django-embed-video

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]