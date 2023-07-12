from django import forms

def validate_name(value):
    if not value[0].isupper():
        raise forms.validationError('name should start with capital letter')

def validate_length(value):
    if len(value)<5:
        raise forms.validationError('length is to short')
    
def validate_age(value):
    if value<18:
        raise forms.ValidationError('age should be greate than 18')

class Student_Form(forms.Form):
    sname=forms.CharField(max_length=100)
    sage=forms.IntegerField()
    semail=forms.EmailField()

