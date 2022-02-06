# dkr-flask-pdb-sandbox
## Overview
Test project to make use of [Python Debugger (pdb)](https://docs.python.org/3/library/pdb.html) from within a dockerised Flask app.


## Virtual Environment Notes
This is a Pipenv project so use the normal pipenv commands to control the virtual environment.


## Docker Cheat Sheet 

```
$ docker build -t dkr-flsk-pdb-sbox .;docker image ls;
...
$ docker container ls --all
...
$ docker rm abdd314c875c
...
$ docker container ls --all
...
$ docker run -p 8787:8787 -d dkr-flsk-pdb-sbox
...
$ docker container ls --all
```
