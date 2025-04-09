from django.contrib import admin
from .models import Article, Comment

# class CommentInline(admin.StackedInline):
class CommentInline(admin.TabularInline):
    model = Comment
    # To display extra comment as fields
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
            CommentInline,
            ]
    list_display = [
        "title",
        "body",
        "author",
    ]

# class CommentAdmin():


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
