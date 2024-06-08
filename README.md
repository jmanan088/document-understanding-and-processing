# AI-Powered Document Understanding and Processing Pipeline



## Installing and Running
 
**Note that you need docker installed to run the setup as this is a containerized app.**

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

## Dependecies
- tesseract-ocr
- Pythin 3.10-slim
- pytesseract
- PyPDF2
- python3-tk (tkinter)
- pdf2image