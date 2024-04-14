from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Class)
admin.site.register(Enrollment)
admin.site.register(Certificate)
# Register your models here.
