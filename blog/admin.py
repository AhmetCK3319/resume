from django.contrib import admin
from blog.models import *


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name','description','slug','updated_at','created_at')
    search_fields = ('name','description','slug')
    list_editable = ('description','slug')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    list_per_page = 25
    prepopulated_fields = {'slug': ('name',)} #slug alanları otomatik olarak doldurulur.

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)



class TagAdmin(admin.ModelAdmin):

    list_display = ('id','name','slug','updated_at','created_at')
    search_fields = ('name','slug',)
    list_editable = ('name','slug')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    prepopulated_fields = {'slug': ('name',)} #slug alanları otomatik olarak doldurulur.

    class Meta:
        model = Tag

admin.site.register(Tag, TagAdmin)



class PostAdmin(admin.ModelAdmin):

    list_display = ('id','title','slug','author','content','excerpt','category',
                    'display_tags','featured_image','status','views_count','published_at',
                    'updated_at','created_at'
                    )
    search_fields = ('title','status','published_at')
    list_editable = ('title','slug','author','content','excerpt','category',
                    'featured_image','status','views_count','published_at',
                     )
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    list_per_page = 25
    prepopulated_fields = {'slug': ('title',)} #slug alanları otomatik olarak doldurulur.

    class Meta:
        model = Post

    def display_tags(self, obj):
        # Bu fonksiyon her yazı için etiketleri birleştirip string olarak döndürür
        return ", ".join([tag.name for tag in obj.tags.all()])

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):

    list_display = ('id','post','name','email','content','is_approved','updated_at','created_at')
    search_fields = ('post','name','email','is_approved')
    list_editable = ('post','name','email','content','is_approved')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    list_per_page = 25
    #prepopulated_fields = {'slug': ('site_name',)} slug alanları otomatik olarak doldurulur.

    class Meta:
        model = Comment

admin.site.register(Comment, CommentAdmin)
