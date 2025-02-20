FROM python:3.9-slim
WORKDIR /app
COPY counter.py /app
RUN mkdir -p /data
CMD ["python", "counter.py"]
