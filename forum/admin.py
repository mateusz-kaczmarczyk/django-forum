from django.contrib import admin
from .models import Subforum, Thread, Comment

admin.site.register(Subforum)
admin.site.register(Thread)
admin.site.register(Comment)