from django import forms


class AddForm(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()
    