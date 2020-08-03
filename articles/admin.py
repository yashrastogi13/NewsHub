from django.contrib import admin

# Register your models here.
from .models import Article,Comment

class CommentInline(admin.TabularInline):
    model = Comment                         # show comment in stacked format
    extra = 0                               # no of empty comments rows = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
     ]
admin.site.register(Article,ArticleAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article_c','comment','author_c','date_c')
    list_filter = ('date_c',)
    search_fields = ('author_c','comment')



