# Django ToDo App 🚀
### Experience a simple but powerful ToDo app with user authentication and seamless CRUD functionality.

<p align="center">
  <img src="base\static\images\am-i-responsive.png" alt="Responsive website" width="600">
</p>

<hr>

## Project Description
The Django Secure Task Management Web Application is designed to provide a simple yet powerful platform for managing personal tasks. The application incorporates user authentication, task creation, editing, deletion, and completion tracking, all within a secure and modular environment. The project prioritizes usability, accessibility, and secure development practices, including proper handling of sensitive data and adherence to secure coding standards. The application’s modular structure ensures maintainability and scalability for future development.

### Languages and Frameworks
This project was created using the following languages and frameworks:

- Django as the Python web framework.
- Python as the backend programming language.
- HTML as the markup language and templating language.
- CSS as the style sheet language.
- Bootstrap 5 as the CSS framework.
- JavaScript to create footer element that changes

## Installation and Running

### Prerequisites
- Python 3.8 or higher (download from python.org)
- Git (cloning purposes)

### Installation Steps
1. Clone the repository:
   - git clone https://github.com/nanactrl/ssd_project.git
   - cd ssd_project

2. Create and activate virtual environment:
   - python -m venv venv
   - Windows: venv\Scripts\activate.bat
   - Mac/Linux:source venv/bin/activate

3. Install dependencies:
   - pip install -r requirements.txt

4. Configure environment variables and edit .env to include your own SECRET_KEY and other configuration values.
   - Windows: copy .env.example .env
   - Mac/Linux: cp. env.example .env
     
5. Apply database migrations:
   - python manage.py migrate

6. Create a superuser (for admin access):
   - python manage.py createsuperuser

7. Start the development server:
    - python manage.py runserver

8. Open the browser and navigate to http://127.0.0.1:8000/ to access the application.

## Security Features Summary

## Task Management Workflow

- All pages have a "Home" button that will take the user back to the homepage. Except for the delete task page, it will only have "go back to task list" button to take the yser back to the full task list.

<p align="center">
  <img src="base\static\images\home-button.png" alt="Home button" width="400">
</p>

- User will redirect to login page where user need to input their username and password. In case user have not registrered themselves as users, they are promted with a text saying "Are you a new user and need to create an account?". A new user needs to click "Register Here" button to register an account.
<p align="center">
  <img src="base\static\images\login.png" alt="Home button" width="400">
</p>

- This is a form that user can fill out the username, password and a re-type the password. But under the form, there is a text promting already created users with the text "Do you already have an account?" and then a "Login" button that takes the user to the login page so that the user can login instead.

<p align="center">
  <img src="base\static\images\register.png" alt="Home button" width="400">
</p>

<p align="center">
  <img src="base\static\images\register-2.png" alt="Home button" width="400">
</p>

- When the login is successful, user will be redirected to the task dashboard. They can view all the task, but for a newly created account, there are no tasks created yet.

<p align="center">
  <img src="base\static\images\task-page.png" alt="Home button" width="400">
</p>

- User can click "Add a task" button to create a new task which will take the user to the create task page. User can create a task by giving the task a title, a description, and then check or uncheck the "completed" checkbox. Leave the checkbox uncheck if it is not done yet.

<p align="center">
  <img src="base\static\images\create-task.png" alt="Home button" width="400">
</p>

- Once the user clicks "Create task" button, they will be redirected back to the task list and can see the task that just being created.

<p align="center">
  <img src="base\static\images\updated-taskpage.png" alt="Home button" width="400">
</p>

- When the task is completed, user can edit the task by clicking on the "gear" icon and edit the task by adding more info to it or marking it as completed. If user mark it as completed, and re-submit, then they will be redirected back to the dashboard and the task is updated with a check-icon, signaling that the task is completed.

<p align="center">
  <img src="base\static\images\complete-task.png" alt="Home button" width="400">
</p>

<p align="center">
  <img src="base\static\images\completed-icon.png" alt="Home button" width="400">
</p>

- If user wish to delete a task, click on the "trash bin" icon and they will be redirected to a confirmation page where it either click on "delete task" or return back to the "main" task page again. If the user clicks on the delete button, it will redicted back to the task list with a succesful deleted task. On the delete confirmation page, there is also a way for the user to "go back to task-list" .

<p align="center">
  <img src="base\static\images\delete-confirmation.png" alt="Home button" width="400">
</p>

- On the homepage, there is text that gives information about the application and also reassures the user that their personal information is secretley kept private and safe.

<p align="center">
  <img src="base\static\images\homepage.png" alt="Home button" width="400">
</p>

- Under the bootstrap carousel, there are two cards - one is prompting the user to login if they already have accounts and one is promting the user to create or register an account incase they have not already done that.

<p align="center">
  <img src="base\static\images\homepage-login-register.png" alt="Home button" width="400">
</p>

- The user can logout from the dashboard whenver they want which takes the user back to the login page.

### Dependencies
Open `requirements.txt` for full list (e.g., Django 4.x, djangorestframework).
