from django.contrib import admin

# Register your models here.
from formapp2.models import Formdata

@admin.register(Formdata)
class FormDataAdmin(admin.ModelAdmin):
  list_display = ('id','username', 'useremail' , 'city')