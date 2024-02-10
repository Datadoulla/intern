FROM python:3.10.13-alpine
WORKDIR .
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]