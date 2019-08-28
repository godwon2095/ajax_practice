from django.contrib import admin
from .models import Item, Like, Review

admin.site.site_header = "Ajax Practice"
admin.site.site_title = "Ajax Practice"

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_diaply_links = (
        'name',
    )

    search_fields = (
        'name',
    )
    
    list_filter = (
    )

    list_display = (
        'name',
        'pk',
        'image',
        'price',
        'created_at',
        'updated_at',
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_diaply_links = (
        'item',
        'user'
    )

    search_fields = (
    )
    
    list_filter = (
        'item',
        'user'
    )

    list_display = (
        'pk',
        'item',
        'user',
        'created_at',
        'updated_at',
    )



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'body',
        'user',
        'item',
        'created_at',
        'updated_at',
    )