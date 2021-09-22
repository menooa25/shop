FROM python:3.9.7-slim-buster
WORKDIR /app
#RUN apt-get update
#RUN apt-get install python3
#RUN apt-get install pip3
COPY requirments.txt ./
RUN pip3 install -r requirments.txt
COPY . ./
CMD ["python3","manage.py","migrate",";",  "python3","manage.py","runserver","--noreload"]
