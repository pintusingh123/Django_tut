from django.contrib import admin
from student.models import PintuData , Result

# Register your models here.

# admin.site.register(PintuData)
# admin.site.register(Result)

class PintuDataAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'roll', 'email', 'city']
  search_fields = ['name', 'roll']
  list_filter = ['city']


admin.site.register(PintuData, PintuDataAdmin)

# result admin way- 1
# class ResultAdmin(admin.ModelAdmin):
#   list_display = ['id', 'name', 'roll', 'marks']
#   search_fields = ['name', 'roll']
#   list_filter = ['marks']

# admin.site.register(Result, ResultAdmin)
# -----------------------


# result admin way- 2 using decorator
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'roll', 'marks']
  search_fields = ['name', 'roll']
  list_filter = ['marks']
