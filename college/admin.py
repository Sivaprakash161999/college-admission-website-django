from django.contrib import admin
from .model import Application, Notice, Detail

# Register your models here.
admin.site.register(Application)
admin.site.register(Notice)
admin.site.register(Detail)
