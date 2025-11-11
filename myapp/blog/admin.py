from django.contrib import admin
from .models import Post,Category,AboutUs

class Postadmin(admin.ModelAdmin):
    list_display=('title','content')
    search_fields=('title','content')
    list_filter=('category','created_at')




# Register your models here.
admin.site.register(Post, Postadmin)
admin.site.register(Category)
admin.site.register(AboutUs)


