FROM python:3.7

# Create app directory
WORKDIR /app

# Install app dependencies
COPY ./requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY dkr-flask-pdb-sandbox /app

EXPOSE 5000
CMD [ "python", "dofl.py" ]
