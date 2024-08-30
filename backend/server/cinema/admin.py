from django.contrib import admin
from .models import Cinema, ScheduledMovie, Ticket

admin.site.register(Cinema)
admin.site.register(ScheduledMovie)
admin.site.register(Ticket)