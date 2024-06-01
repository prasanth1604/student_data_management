Requirements For the project:
1.	Develop a Tool to store the database of students in a school.
2.	Tool Shall have a login and Password.
3.	Tool shall have Admin and User access. (User Would be Teachers)
4.	Tool shall have feature to add the below details of each student:
5.	a.	Name
6.	b.	Gender
7.	c.	Address
8.	d.	Parent Name
9.	e.	Class
10.	f.	Marks
11.	Only Admin shall have access to add/update all the above details of a student.
12.	a.	Teacher shall have access only to edit the marks.
13.	b.	Teacher shall not have any rights to edit any other information of student.
14.	Tool shall provide feature to show the details of students to class teacher.
15.	a.	User (Teacher) shall be able to see students of their class.
16.	b.	User (Teacher) shall be able to generate the details of student in
17.	i.	Word Format
18.	ii.	XML Format


Steps to run the project
Step1: Clone the repository to your local pc
git clone https://github.com/prasanth1604/student_data_management.git

Step2: Enter the directory
cd studentmanagement

Step3: Install required packages
pip install django
pip install pandas
pip install openpyxl

Step4: Run the project
python manage.py runserver

