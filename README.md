# Payroll application APIS

This is sample project code snippet to implement a payroll application,
jwt and django rest framework where introduced. We are implementing a token based authentication 
system based on a role base architecture.

## Installation
Make sure that you have been installed the virtualenv.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install virtualenv.

```bash
pip install virtualenv
```
After the installation, create an env and activate it using the following commands

```bash
virtualenv -p python3 env
```

```bash
source env/bin/activate
```
Navigate to the project folder and install the dependencies given in the requirements,txt file

```bash
pip install -r requirements.txt
```
After the successfull installation do the migrations to reflect the database configurations.

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

## Usage

run the code snippet 

```bash
python manage.py runserver
```
You can navigate to ```http://127.0.0.1:8000/login/``` to test the user 
login, you can use either email or username for login.
You can also run the above scripts using a bash file.
First navigate to the ```run.sh``` file location and give permission for the file 
if doesn't have alreay.
```bash
chmod u+x run.sh
```
then run the run.sh file 

```bash
./run.sh
```

## Testing
Create a superuser to access the admin panel and add some users from there. Also 
should make sure that the user has to be mapped with a user profile object, Because 
we have stored additional information of a user apart from default user model.
[create superuser](https://www.geeksforgeeks.org/how-to-create-superuser-in-django/)

## Testing apis
You can test the apis using postman, or with the help of curl commands.
Navigate to the project root directory, and execute the curl commands given in the 
```apis.txt``` to view the results.

## jwt test
Also you can make sure your resultant token is a valid for a given user in 
[jwt](https://jwt.io/)
