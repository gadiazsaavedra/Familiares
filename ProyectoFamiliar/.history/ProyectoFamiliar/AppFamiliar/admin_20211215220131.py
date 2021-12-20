from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Padres)
admin.site.register(Hijo)
admin.site.register(Conyuge)
admin.site.register(Abuelos)
admin.site.register(Primo)
