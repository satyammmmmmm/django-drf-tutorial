from django.contrib import admin
from testapp.models import Book 
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_Display=['title','author','pages']

admin.site.register(Book,BookAdmin)
