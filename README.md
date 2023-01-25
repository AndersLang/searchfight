## Install Python:

    pyenv install 3.11.0
    pyenv global 3.11.0 # or pyenv local 3.11.0

## Create a virtualenv and install dependencies

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    pip install -r requirements_dev.txt


## Google api key
    AIzaSyCuvspD4FwH77YSlKP7Es0L8hIEjYRorDQ

## Google Search api example url

    GET https://www.googleapis.com/customsearch/v1?key=AIzaSyCuvspD4FwH77YSlKP7Es0L8hIEjYRorDQ&cx=2461c1029c04d4c41&q=lectures

## Google cx value
    cx=2461c1029c04d4c41

## USAGE
To search for "lectures" and "python" use below command.

    python search_fight.py -st lectures -st python