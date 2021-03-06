FROM python:3.7.1-slim

COPY ["./requirements.txt", "/usr/src/"]
WORKDIR /usr/src/
RUN pip install --no-cache-dir -r requirements.txt

COPY [".", "."]

CMD ["python", "main.py"]