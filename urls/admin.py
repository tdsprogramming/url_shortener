# django imports
from django.contrib import admin

# project imports
from .models import Url

# register model to admin
admin.site.register(Url)
