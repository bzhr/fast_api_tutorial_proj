# Damilah applicaton project
This is my solution for the oauth app project task for the Python software engineer at Damilah.

## Setting up the project
I use [pyenv](https://github.com/pyenv/pyenv) to setup the virtual env and install the specific python version. The project should work with most recent versions of Python and you don't have to use pyenv to create the virtual env, if you prefer something else.
1. Create a virtualenv for the project: `pyenv virtualenv 3.12.2 damilah`
2. `cd` into the project and run: `pyenv local damilah`. This command connects the virtualenv to the project folder. When you `cd` into the project folder the virtualenv will automatically be activated. Also, the editors, like VSCode will automatically activate the right virtualenv.
3. Install third party libraries from the requirements file: `pip install -r requirement.txt`
4. Install third party dev libraries from the dev requirements file: `pip install -r requirement.txt`.
5. Modify env.example to .env and update the variables inside if needed.
6. Run the app: `uvicorn main:app --reload`

## The API chosen and its authentication steps
This app works with the Github OAuth API, so you will need to register an app from the "developers" tab in the settings of your Github settings. Once you create the app, you need to generate the "client secret" and store it in a safe place. The app client id and client secret are needed for the authentication process. These are stored as enviroment variables in the system or in the .env file.
## Instructions on how to run the script
Run the app: `uvicorn main:app --reload`
## A brief explanation of the implemented design pattern.
