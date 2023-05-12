from django import forms
from .models import Cities, Departments


# Відділи, Департаменти:
class DepsForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields = 'department'


# Міста:
class CitiesForm(forms.ModelForm):
    class Meta:
        model = Cities
        fields = 'city'

# Just for Example:
# class PostForm(forms.ModelForm):
#     # Meta class - class returning another class
#     class Meta:
#         model = Post
#         fields = ('title', 'about', 'content', 'author', 'image', 'source')
#
#
# class PostForm2(forms.ModelForm):
#     # Meta class - class returning another class
#     class Meta:
#         model = Post
#         fields = ('title', 'about', 'content', 'author', 'source')
