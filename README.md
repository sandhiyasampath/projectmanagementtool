# projectmanagementtool
1. This project management tool supports the following features
    1. Ability to create, update and delete Employees
    2. Ability to create, update and delete Projects
    3. Ability to assign and dissociate Employees to Projects

2. Pre-requisite:
    1. Make sure you have installed Python3, Django, pip, mysql in your system
    2. Create schema projectManagement in your system
    3. Run the below command to create the reuired tables in the database
        1. python manage.py makemigrations
        2. python manage.py migrate
        3. python manage.py createsuperuser(to create user to access django admin)

    4. Run the below code to run the application
        1. python manage.py runserver 

3. Admin can do CRUD(Creat Read Update Delete) operations by using below mentioned Link
    http://127.0.0.1:8000/admin/register/
    Note : Use the credential created in step 2.iii.c to login to django admin page

4. Also can see the Employee Records and Details by using below link
    http://127.0.0.1:8000/

    Note: Please create some employees and projects to access it.

Bonus-Point
    1.Implemented Case insensitive Search
    2.It will not work for partial search
    3.if you given any wrong input it will show you the proper message
    4.Not implemented Percentage allocations
    


