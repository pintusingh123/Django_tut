from django import forms


class StudentForm(forms.Form):
  f_name=forms.CharField(label='First Name', max_length=70)
  l_name=forms.CharField(label='Last Name', max_length=70)
  email=forms.EmailField(label='Email' , max_length=70)
  city=forms.CharField(label='City', max_length=70)

  