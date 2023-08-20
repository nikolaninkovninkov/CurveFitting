FROM  python:3.11.4-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:$PORT