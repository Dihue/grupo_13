from django.contrib import admin

from .models import Post, Comment, Categoria

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Comment)


