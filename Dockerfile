FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
EXPOSE 8586
CMD python ./app.py


