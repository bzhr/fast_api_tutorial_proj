# Damilah applicaton project
This is my solution for the oauth app project task for the Python software engineer at Damilah.

## Setting up the project
I use [pyenv](https://github.com/pyenv/pyenv) to setup the virtual env and install the specific python version.
1. Create a virtualenv for the project: `pyenv virtualenv 3.12.2 damilah`
2. `cd` into the project and run: `pyenv local damilah`. This command connects the virtualenv to the project folder. When you `cd` into the project folder the virtualenv will automatically be activated. Also, the editors, like VSCode will automatically activate the right virtualenv.
3. Install third party libraries from the requirements file: `pip install -r requirement.txt`
4. Install third party dev libraries from the dev requirements file: `pip install -r requirement.txt`.
4. Run the app: `uvicorn main:app --reload`

## The API chosen and its authentication steps
## Instructions on how to run the script
Run the app: `uvicorn main:app --reload`
## A brief explanation of the implemented design pattern.
