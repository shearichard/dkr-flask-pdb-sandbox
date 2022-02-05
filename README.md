# dkr-flask-pdb-sandbox
Test project to make use of pdb from within a dockerised Flask app.


# Virtual Environment Notes
This is a Pipenv project so use the normal pipenv commands to control the virtual environment.


# Docker Cheat Sheet Memory jogger

```
(dkr-flask-pdb-sandbox) rshea@mayari:~/src/dkr-flask-pdb-sandbox/flskapp$ docker container ls --all
...
(dkr-flask-pdb-sandbox) rshea@mayari:~/src/dkr-flask-pdb-sandbox/flskapp$ docker rm abdd314c875c
...
(dkr-flask-pdb-sandbox) rshea@mayari:~/src/dkr-flask-pdb-sandbox/flskapp$ docker container ls --all
...
(dkr-flask-pdb-sandbox) rshea@mayari:~/src/dkr-flask-pdb-sandbox/flskapp$ docker run -p 5000:5000 -d dkr-flsk-pdb-sbox
...
(dkr-flask-pdb-sandbox) rshea@mayari:~/src/dkr-flask-pdb-sandbox/flskapp$ docker container ls --all
```
