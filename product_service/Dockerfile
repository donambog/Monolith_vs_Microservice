# product_service/Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY product_service.py /app/
RUN pip install flask
CMD ["python", "product_service.py"]
