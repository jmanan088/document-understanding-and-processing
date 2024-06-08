FROM python:3.10-slim

WORKDIR /code

RUN apt-get update

RUN apt-get install -y tesseract-ocr

RUN apt-get clean

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

CMD [ "python" , "src/image_to_text/ocrimage.py" ]