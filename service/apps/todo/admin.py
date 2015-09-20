from django.contrib import admin
from models import TodoTask

class TodoTaskAdmin(admin.ModelAdmin):
    list_display = ["uuid", "who", "task", "due", "done"]

admin.site.register(TodoTask, TodoTaskAdmin)
