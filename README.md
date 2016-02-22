# Social todo Django starter code

Hello! Welcome to my second social to-do app! This time, it was created with
Django. 

Similar to the last app, for the foundation, I used the starter code
provided by Kyle via github repository. After cloning the repository, I 
began building the other functions. 

First, when you come to the index page, you'll be prompted with two different
options. Either login, or register. These are filled with different fields--
name, email, password, and password confirmation fields for the register field;
email and password for the login field.

After logging in or registering successfully, you'll be directed to the tasks 
index, where you will see a todo list. In this todo list, you will see a list
of tasks that you will have previously submitted and the description italicized.

Below this list, you will see various blanks where you can input new tasks.
You could input the task title, description, and various collaborators' emails.

If you input emails of collaborators, this task should pop up on the todo list of
the collaborators. 

After completing tasks, you can choose to either delete or mark as complete 
each task. 

---

We wrote this in office hours. It defines the models for tasks,
migrations, etc. It is based on the 
[Django tutorial](https://docs.djangoproject.com/en/1.9/intro/).

To install this on c9, clone the repository. Then, before you run it
for the first time, you'd do

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
This installs your Python dependencies. Then you need to run your database
migrations with 

```
python manage.py migrate
```

This will create a file called `db.sqlite3`, which is ignored in your
`.gitignore` file. 

Now you're ready to run the application.Then you can run it with the following

```
python manage.py runserver 0.0.0.0:$PORT
```

Then you can click "Preview" in the c9 interface to see your running application.
Off to the races.