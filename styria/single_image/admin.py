from django.contrib import admin
from models import Image, Comment, Rating


class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_file', 'description', )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'image')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating', 'image')


admin.site.register(Image, ImageAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Rating, RatingAdmin)