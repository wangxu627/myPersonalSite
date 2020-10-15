---
title: "Create Requiremnt.txt Using Pipenv"
date: 2020-10-15T10:55:18+08:00
Description: ""
Tags: []
Categories: []
DisableComments: false
---

# Instilling pipenv

Run the following in your terminal for a user installation:
```
pip install --upgrade setuptools wheel
pip install --user pipenv
```

After installation, open a new terminal and run pipenv
```
> pipenv
Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --where             Output project home information.
  --venv              Output virtualenv information.
  --py                Output Python interpreter information.
  --envs              Output Environment Variable options.
  ...
```

If you however get 'pipenv' is not recognized as an internal or external command, operable program or batch file, get the Python path to the base directory for the user site-packages by running:
```
python -m site --user-site
```

Replace site-packages in the path with Scripts then add to your system PATH (on Windows: Edit environment variables for your account > in the User variables select Path > Edit > New > `C:\Users\drgabrielharris\AppData\Roaming\Python\Python37\Scripts` ). For more details check here

# Using pipenv to install packages 📦

Navigate to your project directory and run:
```
pipenv shell
```

This does few things for you:
* Creates a virtualenv for this project using the activated/registered Python interpreter in the current terminal. The virtualenv is created in the folder C:\Users\<username>\.virtualenvs and is given a name automatically

* Creates a Pipfile in the project’s directory. The Pipfile is used to track which dependencies your project needs in case you need to re-install them

* Launches a subshell in the project’s directory (i.e. activating the virtualenv)

Now you can install all the required packages as you would usually do using pip but using pipenv instead, for example:
```
pipenv install pandas
```

Once you have finished, run your script to check that you’ve indeed installed everything that is required:
```
pipenv run python script.py
```

 # Creating requirements.txt 📃
This’s what you’ve been waiting for!
```
pipenv lock -r > requirements.txt
```

This creates a `Pipfile.lock` file (or updates an existing one) in the project’s directory, and of course your `requirements.txt` file with the required dependencies:
```
-i https://pypi.org/simple
numpy==1.18.1
pandas==1.0.1
python-dateutil==2.8.1
pytz==2019.3
six==1.14.0
```

## Useful to know
To uninstall a package
```
pipenv uninstall <package-name>
```

To remove the virtual environment
```
pipenv --rm
```

To see dependencies
```
pipenv graph
```

# What is next? 👊
Learn how to use your `requirements.txt` to build a Docker image [👉](https://medium.com/swlh/python-how-starting-with-docker-d2be73d9ae92)

Happy coding!
