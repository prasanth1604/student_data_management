from django import template
from students.models import Student ,Subject , Faculty

register = template.Library()

def searchName(value):
    st = Student.objects.get(roll_no=value)
    return st.name