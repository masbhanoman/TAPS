from django.contrib import admin

# Register your models here.

from .models import Post, post_type

class post_typeAdmin(admin.ModelAdmin):
    model = Post
    #filter_horizontal = ("posts",)



admin.site.register(Post)
admin.site.register(post_type, post_typeAdmin)

