from django. urls import path
from .views import item_show, like_toggle, create_review, delete_review

app_name = 'items'
urlpatterns = [
    path('<int:item_id>/', item_show, name="show"),
    path('<int:item_id>/like_toggle/', like_toggle, name="like_toggle"),
    path('<int:item_id>/create_review/', create_review, name="create_review"),
    path('<int:review_id>/delete_review/', delete_review, name="delete_review"),
]
