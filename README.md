# AI-Powered Document Understanding and Processing Pipeline

**Note that you need docker installed to run the setup as this is a containerized app.**

This project uses a `python 3.10-slim` docker image.

## Installing and Running
 


First clone the repository. Then read the below text for setup instructions.

Docker containers doesn't have GUI so we need to setup X Server in windows and allow docker to connect to it to diplay GUI. For this I'm using **VcXsrv Windows X Server**. 
You can install it buy running command:
```
choco install vcxsrv
```

After that go to [docker-compose](./docker-compose.yml) file and set `YOUR_IP` to local IP address. Which cna be found by typing ipconfig  in cmd and selecting IPv4 address.

Then run Xlaunch from the start menu and disable access control to allow docker container to connnect.
You can follow [this tutorial]("https://dev.to/darksmile92/run-gui-app-in-linux-docker-container-on-windows-host-4kde") to help you setup.


To run the app type below command in powershell/terminal of root directory. 


```
docker-compose up --build
```

> Put all the PDF files that you want to run in the folder named test.

## Result
After browsing the PDF, you can get all the text from [`out_text`](./src/out/out_text.txt) file.
And asking the question in chat, you can get answer for specifics.

> You can also see the accuracy in terminal output you started the docker container in, along with word number and page number.

## Libraries Used
- tesseract-ocr
- pytesseract
- python3-tk (tkinter)
- pdf2image
- LayoutXLM
- DocQuery