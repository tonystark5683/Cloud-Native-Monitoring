FROM python:3.9-slim-buster 
# Creating Python Image

WORKDIR /app
# working Directory
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
#for installing the pakages
COPY . . 
#copy the code to the docker working directory
ENV FLASK_RUN_HOST=0.0.0.0
# set the envrnmt var
EXPOSE 5000

CMD ["flask","run"]
# run the app

#work flow of doccker first we crewate a docker file 
# then build the docker image and then run the docker container