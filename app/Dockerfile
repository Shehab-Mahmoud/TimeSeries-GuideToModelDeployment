# the image we are basing the container on
FROM python:3.8

# COPY excutes on the host machine
RUN mkdir -p /home/app
WORKDIR /home/app
COPY . /home/app/
ENV FLASK_APP=/home/app/app.py
# runs linux commands and excutes in the container
RUN pip install -r /home/app/requirements.txt 

# entry point command - marks for docker file that this is
# the command you excute as an entry point
EXPOSE 5000
CMD ["flask","run","--host=0.0.0.0","--port=5000"]

