from django.contrib import admin
from models import Blogpost,Question,Choice


# Register your models here.
#the presentation of a model in the admin interfacxe
class BlogpostAdmin(admin.ModelAdmin):
    #field name to exclude from the form
    exclude=["posted"]
    #the given fields will use a bit of JavaScript to populate from the fields assigned
    prepopulated_fields = {'slug':('title',)}
admin.site.register(Blogpost,BlogpostAdmin)
admin.site.register(Question)
admin.site.register(Choice)
