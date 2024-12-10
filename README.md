# Task Manager Project

The project will solve possible problems during product development by your team.

Each team member can create a task, assign that task to other team members, and mark it as completed.

## Check it out!

[Task manager project deployed to Render]

https://task-manager-deploy-ov24.onrender.com

- You can use following user (or create another one by yourself):
  - Login: `test.user`
  - Password: `1qazcde3`

## Installation

Python3 must be already installed

Create a `.env` file following the `.env.sample` template and replace with your values.

```shell
git clone https://github.com/VladyslavBon/Task_Manager
cd Task_Manager

python3 -m venv venv
- For Linux or Mac:
    source venv/bin/activate
- For Windows:
    source venv/Scripts/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Features

* Authentication functionality for Worker/User
* Managing tasks directly from website interface
