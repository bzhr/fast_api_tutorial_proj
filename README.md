# Damilah applicaton project
This is my solution for the oauth app project task for the Python software engineer at Damilah.

## Setting up the project
I use [pyenv](https://github.com/pyenv/pyenv) to setup the virtual env and install the specific python version. The project should work with most recent versions of Python and you don't have to use pyenv to create the virtual env, if you prefer something else.
1. Create a virtualenv for the project: `pyenv virtualenv 3.12.2 damilah`
2. `cd` into the project and run: `pyenv local damilah`. This command connects the virtualenv to the project folder. When you `cd` into the project folder the virtualenv will automatically be activated. Also, the editors, like VSCode will automatically activate the right virtualenv.
3. Install third party libraries from the requirements file: `pip install -r requirement.txt`
4. Install third party dev libraries from the dev requirements file: `pip install -r requirement.txt`.
5. Modify env.example to .env and update the variables inside if needed. To make it easier for you, I've decided to upload this project with my registered app credentials. You can run directly the project after installing the requirements.
6. Run the app: `uvicorn main:app --reload`
7. For development pre-commit is used and it is installed in step 4. For development to set it up run: `pre-commit install`. `ruff` is used for both linting and formatting. The custom rules can be found in the `pyproject.toml` file.

## The API chosen and its authentication steps
This app works with the Github OAuth API, so you will need to register an app from the "developers" tab in the settings of your Github settings. Once you create the app, you need to generate the "client secret" and store it in a safe place. The app client id and client secret are needed for the authentication process. These are stored as enviroment variables in the system or in the .env file. Currently the project runs with my own creds, so you don't have to register the Github app.
## Instructions on how to run the script
Run the app: `uvicorn main:app --reload`
## A brief explanation of the implemented design pattern.
I've chosen the Adapter pattern in order to adapt the `requests` library and provide a clean interface for making requests to the Github API.
> “The Adapter Pattern allows incompatible interfaces to work together by wrapping one with another expected interface.”

Why this pattern?
- Decouples your code from third-party libraries
- Simplifies testing (you can mock your adapter instead of the library)
- Makes refactoring easier (swap out the library without changing your app logic)
