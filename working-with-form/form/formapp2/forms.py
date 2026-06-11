from django import forms
from django.core import validators


class StudentData(forms.Form):

    name = forms.CharField(
        label='Name',
        max_length=70,
        error_messages={"required":"enter name pls"},
        validators=[
            validators.MaxLengthValidator(13),
            validators.MinLengthValidator(3)
        ]
    )
    email = forms.EmailField(
        label='Email',
        max_length=70
    )
    city = forms.CharField(
        label='City',
        max_length=70,
        
    )


#  single time validation cheking
#     def clean(self):
#         cleaned_data = super().clean()
#         name_value = cleaned_data.get('name')
#         email_value = cleaned_data.get('email')
#         if name_value and len(name_value) < 4:
#             self.add_error("name", "enter more than 4 char")
#         if email_value and len(email_value) < 13:
#             self.add_error("email", "enter more than 13 char")
#         return cleaned_data


# # fun for crean fielding validation
# # def clean_name(self):
#     #    name_value = self.cleaned_data['name']
#     #    if len(name_value) < 4:
#     #       raise forms.ValidationError("please enter more then or equal 4 name char ")
#     #    return name_value

# # def clean_email(self):
#         email_value = self.cleaned_data['email']
#         if len(email_value) < 13:
#             raise forms.ValidationError("pls enter more than or equal 5 char")
#         return email_value
