from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from blogapi.blog.models import Tag, Post, Author

class AuthorInline(admin.StackedInline):
    model = Author
    can_delete = False
    verbose_name_plural = 'author'

class UserAdmin(BaseUserAdmin):
    inlines = (AuthorInline,)

class PostAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
