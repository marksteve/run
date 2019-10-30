FROM python:3.7
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
ENV PORT 8000
CMD exec gunicorn -b 0.0.0.0:$PORT -w 2 main:app
