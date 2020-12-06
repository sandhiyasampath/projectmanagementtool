# projectmanagementtool
1. This project management tool supports the following features
    1. Ability to create, update and delete Employees
    2. Ability to create, update and delete Projects
    3. Ability to assign and dissociate Employees to Projects

2. Pre-requisite:
    1. Make sure you have installed Python3, Django, pip, mysql in your system
    2. Create schema projectManagement in your system
    3. Run the below command to create the reuired tables in the database
        a. python manage.py makemigrations
        b. python manage.py migrate
        c. python manage.py createsuperuser(to create user to access django admin)

    4. Run the below code to run the application
        a. python manage.py runserver 

3. Admin can do CRUD(Creat Read Update Delete) operations by using below mentioned Link
    http://127.0.0.1:8000/admin/register/
    Note : Use the credential created in step 2.3.c to login to django admin page

4. Also can see the Employee Records and Details by using below link
    http://127.0.0.1:8000/

    Note: Please create some employees and projects to access it.


