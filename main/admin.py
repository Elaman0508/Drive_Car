from django.contrib import admin
from sign_in.models import CustomUser
from main.models import Car


admin.site.register(Car)
admin.site.register(CustomUser)
