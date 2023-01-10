# Django Reboot

After 10 years not really using Django, I need some time to review the technology I used before:

## Virtual Environment

Django advise to run in virtual environment. 

Setup a virtual environment:

> py -m venv venv

Create a Virtual Environment named venv, after that you will find a new folder .venv, there are some scripts.

Activate the virtual environment and then enter to the virtual environment:
> .venv\Scripts\Activate.ps1

Install Django

> (.venv) py -m pip install django~=4.0.0

Initiate Django project where it creates a few files which sufficient to run a web service

> (.venv) > django-admin startproject django_project .


Run the project

> py manage.py runserver

A default website is up and can be access via http://localhost:8000

### Migration

A warning regarding: 18 unapplied migrations

We have not yet 'migrated' our initial database. Run below command and Django creates a SQLite database and migrated it built-in apps provided for us. A new file db.sqlite3 created
> py manage.py migrate

It will create a file db.sqlite3

### Create an app

Django project is a holder for applications. We always need an app to our logic. To create an app:

> py manage.py startapp pages

Above command create an app name 'pages'. A folder named 'pages' was created after run above command, it contains basic files of an app. [Further read](https://docs.djangoproject.com/en/4.1/ref/request-response/)

## Problems

Hitting below error:
PS C:\projects\pocs> cd .\poc-django\
PS C:\projects\pocs\poc-django> py -m venv venv
PS C:\projects\pocs\poc-django> .\venv\Scripts\activate
.\venv\Scripts\activate : File C:\projects\pocs\poc-django\venv\Scripts\Activate.ps1 cannot be loaded because running
scripts is disabled on this system. For more information, see about_Execution_Policies at
https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ .\venv\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException

Root Cause: [Execution Policy](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.3)

See the [solution](https://stackoverflow.com/questions/24067409/powershell-execution-policy-is-restricted-but-only-when-run-through-python), run below command in powsershell:

> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

## References

[https://djangoforbeginners.com/hello-world/][def]

[def]: https://djangoforbeginners.com/hello-world/