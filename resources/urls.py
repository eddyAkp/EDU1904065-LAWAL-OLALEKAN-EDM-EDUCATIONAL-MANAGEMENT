from django.urls import path
import resources.views as resources_views


urlpatterns = [
    path("", resources_views.InventoryListView.as_view()),
    path("<str:resource_type>/<str:resource_id>/", resources_views.get_stock_count),
]