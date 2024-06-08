FROM python:3.10-slim

WORKDIR /code

RUN apt-get update && \
    apt-get install -y tesseract-ocr && \
    apt-get install -y python3-tk && \
    apt-get clean && \
rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src
ENV PYTHONPATH ./src

CMD [ "python" , "src/app/app.py" ]