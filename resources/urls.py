from django.urls import path
import resources.views as resources_views


urlpatterns = [
    path("", resources_views.InventoryListView.as_view()),
]