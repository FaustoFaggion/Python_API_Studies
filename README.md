# Python_API_Studies
Python API

## Links

    https://realpython.com/api-integration-in-python/#rest-apis-and-web-services


## Flask (https://realpython.com/introduction-to-flask-part-1-setting-up-a-static-site/)

### Requirements

    Python 2.7:
        $ sudo apt update
        $ sudo apt install python2

    pip:
        $ sudo apt update
        $ sudo apt install python3-pip

    virtualenv:
        $ python3 -m venv .venv
            This will create the .venv directory if it doesn’t exist, and also create directories inside it containing a copy of the Python interpreter and various supporting files.

### Start

    * Create  dir backend inside repository
    * Install venv into dir backend
    * Active virtualenv
      * $ source backend/bin/active
    * Install Flask
      * $ pip install Flask


# TESTS

## PyTest

### Installl

    $ sudo pip install pytest


# ANGULAR

## Install

    ```  
    # install nvm (Node Version Manager)
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash

    # download and install Node.js (you may need to restart the terminal)
    nvm install 22

    # verifies the right Node.js version is in the environment
    node -v # should print `v22.12.0`

    # verifies the right npm version is in the environment
    npm -v # should print `10.9.0`
    ```
    ```
    npm install -g @angular/cli
    ```