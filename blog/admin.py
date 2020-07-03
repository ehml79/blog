from django.contrib import admin
from .models import Post, Category, Tag
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    # list_display 属性控制 Post 列表页展示的字段。
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    #  fields 属性，则用来控制表单展现的字段
    fields = ['title', 'body', 'excerpt', 'category', 'tags']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)