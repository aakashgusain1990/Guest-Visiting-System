from django.contrib import admin

# Register your models here.
from .models import User
admin.site.register(User)

from .models import Security_db
admin.site.register(Security_db)

from .models import Faculty_db
admin.site.register(Faculty_db)

from .models import Details_db
admin.site.register(Details_db)

from .models import Appointments_db
admin.site.register(Appointments_db)