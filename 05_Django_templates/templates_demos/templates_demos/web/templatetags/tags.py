from django.template import Library

register = Library()


@register.simple_tag(name='student_info')
def show_student_info(student):
    return f'Hello, My name is {student.name} and I am {student.age}-years.'
