# Starting environment

To work with python we have first to create a virtual enviroment to hold our project, to do it you will navagate to the project directory on the terminal and run the following command (keep on mind the python3 and pip have to be previously installed):

`python -m venv env`

> Command used to create the virtual environment

`. env/bin/activate`

> Command used to activate our virtual env

`pip install -r requirements.txt`

> Command used to install all required libraries

`python manage.py runserver`

> This command will run the application, now if you enter the http://127.0.0.1:8000 you should see our application running on your browser