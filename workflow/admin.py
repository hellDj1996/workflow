from django.contrib import admin

# Register your models here.
from .models import Workflow, AlertScript, State, Transition

admin.site.register(Workflow)
admin.site.register(AlertScript)
admin.site.register(State)
admin.site.register(Transition)