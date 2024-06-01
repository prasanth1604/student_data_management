
# Student database Management

A brief description of what this project does and who it's for

Requirements For the project:

Develop a Tool to store the database of students in a school.
Tool Shall have a login and Password.
Tool shall have Admin and User access. (User Would be Teachers)
Tool shall have feature to add the below details of each student:

a. Name

b. Gender

c. Address

d. Parent Name

e. Class

f. Marks

Only Admin shall have access to add/update all the above details of a student.

a. Teacher shall have access only to edit the marks.

b. Teacher shall not have any rights to edit any other information of student.

Tool shall provide feature to show the details of students to class teacher.

a. User (Teacher) shall be able to see students of their class.

b. User (Teacher) shall be able to generate the details of student in

i. Word Format

ii. XML Format


# Steps to run the project 

### Step1: Clone the repository to your local 
pc git clone https://github.com/prasanth1604/student_data_management.git

### Step2: Enter the directory 
cd studentmanagement

### Step3: Install required packages 
pip install django 
pip install pandas 
pip install openpyxl

### Step4: Run the project python manage.py runserver
