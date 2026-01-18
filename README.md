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

- When the login is successful, user will be redirected to the "main application". For a newly created account, there are no tasks created yet.

- Click "add a task" button to create a task. This will redirect user to a page where they can create a task by giving it a title, description and a check or un-check status. Leave the checkbox uncheck if it is not done yet.

- After submitting the task, user will be redirected back to the task-list where they can see the newly created task.

- When the task is completed, user can edit the task by clicking on the "gear" icon and edit the task by adding more info to it or marking it as completed. If user mark it as completed, and re-submit, then they will be redirected back to the task-list and the task is updated with a check-icon, signaling that the task is completed.

- If user wish to delete a task, click on the "trash-bin" icon and they will be redirected to a confirmation page where it either click on "delete task" or return back to the "main" task page again.
  
## Features

- Register an account which require user to enter a username and a password.

- All the pages have a "home" button that takes the user back to the homepage - except the "delete-task"-page - that page only haves a "go back to task list" button that can take the user back to the full-task-list.

<p align="center">
  <img src="base\static\images\home-button.png" alt="Home button" width="400">
</p>

- User will redirect to login page where user need to input their username and password. In case user have not registrered themselves as users, they are promted by a text saying "Are you a new user and need to create an account?". The "Register Here" button will take the user to the register user page.
<p align="center">
  <img src="base\static\images\login.png" alt="Home button" width="400">
</p>

- The same as above, but for the register-user-page. There is a form that the user can fill out with username and then a password and a re-type for the password - and of course a button that says "register". But under that form, there is a text promting already created users with the text "Do you already have an account?" and then a login-button that takes the user to the login-page so that the user can login instead.

<p align="center">
  <img src="base\static\images\register.png" alt="Home button" width="400">
</p>

<p align="center">
  <img src="base\static\images\register-2.png" alt="Home button" width="400">
</p>


- When a user has logged-in successfully - then the user is redirected to their task-dashboard. Here they can view all their tasks.

<p align="center">
  <img src="base\static\images\task-page.png" alt="Home button" width="400">
</p>

- They can click on the button "Add a task" to create a new task which will take the user to the create-task-page. Here the user can create a task by giving the task a title, a description (or not) and then uncheck or check the "completed" check-input.

<p align="center">
  <img src="base\static\images\create-task.png" alt="Home button" width="400">
</p>

- Once the user clicks on "Create" then the user is re-directed back to the task-list and they can now see their task they just created.

<p align="center">
  <img src="base\static\images\updated-taskpage.png" alt="Home button" width="400">
</p>

- When a user is at the dashboard (task-list), they can also delete and edit the task. To be able to edit a task the user can click on the button next to the task (settings-icon) and then the user is redirected to the task and the form for that specific task. The user can edit any of the field and re-submit/edit the task. They can for example klick on the "completed" check-box and then resubmit and then the user is redirected to the dashboard and now the user can see a "tick"/check next to the task which is giving a visual sensation of completion which is a choise for a good UX.

<p align="center">
  <img src="base\static\images\complete-task.png" alt="Home button" width="400">
</p>

<p align="center">
  <img src="base\static\images\completed-icon.png" alt="Home button" width="400">
</p>

- The user can also delete tasks by clicking on the "trash-bin-icon" next to the task - this will redirect the user to a confirmation-page where the user is given a question if the user wants to delete the task - if the user clicks on the delete button, then the user is redicted back to the task-list with a succesful deleted task. On the delete-confirmation page, there is also a way for the user to "go back to task-list" incase the user regretted their choise - which is part of good UX aswell.

<p align="center">
  <img src="base\static\images\delete-confirmation.png" alt="Home button" width="400">
</p>

- The user can whenever they want logout from the dashboard which takes the user back to the login-page.

- On the homepage there is text that gives information about the application and also reassures the user that their personal information is secretley and kept private and safe - this gives the user trust for the service and application. Under that section, there is a carousel giving a "high-tech" feeling towards the appliction - the pictures are not of the application itself but just placeholder images that gives a good design and modern feeling towards the webpage/application.

<p align="center">
  <img src="base\static\images\homepage.png" alt="Home button" width="400">
</p>

- Under the bootstrap carousel, there are two cards - one is prompting the user to login if they already have accounts and one is promting the user to create or register an account incase they have not already done that.

<p align="center">
  <img src="base\static\images\homepage-login-register.png" alt="Home button" width="400">
</p>

- Under this section comes the footer - here is a copyright promt and two icons - one for my personal GitHub nad one for my personal LinkedIn profile.

<p align="center">
  <img src="base\static\images\footer.png" alt="Home button" width="400">
</p>

<hr>

### Dependencies
Open `requirements.txt` for full list (e.g., Django 4.x, djangorestframework).

#### UX design
The UX design of the Django ToDo App focuses on simplicity and ease of use. Here’s a brief overview of the key design elements:

#### Simplicity and Essential Features

The app is designed to include only the essential features needed for managing tasks. This keeps the interface clean and straightforward, making it easy for users to navigate and manage their tasks without unnecessary distractions.

#### Clear Visual Contrast

We carefully selected colors to ensure good contrast between text and backgrounds, making the app easy to read and accessible to all users. This enhances the overall user experience, especially for those with visual impairments.

#### Readable Fonts and Intuitive Icons

Fonts were chosen for their clarity, ensuring that text is easy to read on any device. Icons are intuitive and guide users through the app, making actions like editing or deleting tasks simple and understandable.

#### Mobile-Friendly Design

The app was built with a mobile-first approach, ensuring that it looks and works great on both mobile devices and desktops. The layout adapts smoothly to different screen sizes, providing a consistent experience across all devices.

#### User Feedback and Navigation

The app provides clear feedback on user actions, such as marking tasks as complete with a checkmark. Navigation is straightforward, with all pages including links to return to the task list or homepage, so users never have to rely on the browser’s back button.

In summary, the UX design of the Django ToDo App prioritizes simplicity, clarity, and accessibility, making task management easy and enjoyable for all users.

<p align="center">
  <img src="base\static\images\1.png" alt="first page mockup" width="400">
</p>
- This is the initial mockup for the application and it shows a user hich is not logged in or authenticated - then the user is taken to the homepage and only gets displayed the homepage, which only leads to the loginpage or the signup/register page.

<p align="center">
  <img src="base\static\images\2.png" alt="tasklist" width="400">
</p>
- This mockup shows a user who is authenticated or logged in - the user gets to see their tasks that are savedto the database. From this initial mockup the user can navigate to the homepage again and also log itself out. To the actual project, we added the delete functionality here and also a text displaying to the user how many incomplete tasks the user currently has.

<p align="center">
  <img src="base\static\images\3.png" alt="edit / add task" width="400">
</p>
- On this page, the use can edit or create a task. The user can also get the ability to mark a task as completed.

<hr>

<p align="center">
  <img src="base\static\images\database-models.png" alt="database models" width="400">
</p>

## Credits
- Comprehensive resource for in-depth understanding of Django class-based views: [ccbv.co.uk](https://ccbv.co.uk/)

- Reference materials aiding comprehension of `get_context_data` in Django: [Django Forum Thread](https://forum.djangoproject.com/t/get-context-data-only-users-data/3904/7)

- Utilized color schemes from [Color Hunt](https://colorhunt.co/) to enhance page aesthetics.

- Leveraged [Heroku Dev Center](https://devcenter.heroku.com/categories/reference) documentation for debugging purposes.

- Incorporated Google Fonts icons from [Google Fonts](https://fonts.google.com/icons) for iconography throughout the application.
