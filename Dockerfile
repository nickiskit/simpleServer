FROM python:3-alpine
WORKDIR /app
COPY ./project /app
EXPOSE 9000
CMD ["python3", "server.py"]
