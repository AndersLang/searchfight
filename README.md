## Install Python:

    pyenv install 3.11.0
    pyenv global 3.11.0 # or pyenv local 3.11.0

## Create a virtualenv and install dependencies

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    pip install -r requirements_dev.txt