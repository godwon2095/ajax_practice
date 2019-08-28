from django.contrib import admin
from django. urls import path
from items.views import item_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', item_list, name="root_page"),
]
