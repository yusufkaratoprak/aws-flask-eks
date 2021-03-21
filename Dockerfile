FROM python:3.7-alpine
RUN mkdir /app
WORKDIR /app
ADD ./app /app/
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "/app/main.py"]