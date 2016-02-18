from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description', max_length=100)
    collaborators = forms.CharField(label='Collaborators', max_length=100)