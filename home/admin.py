from django.contrib import admin
from home.models import info, facultyt, securityt,role, visitort, appointments 
# Register your models here.
admin.site.register(facultyt)
admin.site.register(visitort)
admin.site.register(role)
admin.site.register(securityt)
admin.site.register(info)
admin.site.register(appointments)