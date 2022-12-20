import itertools

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from resources.models import (AudioVisualMaterial, PrintMediaMaterial)


# Create your views here.


class InventoryListView(generic.ListView, LoginRequiredMixin):
    context_object_name = "resources"
    template_name = "inventory/inventory_list_view.html"

    def get_queryset(self):
        return list(
            itertools.chain(
                AudioVisualMaterial.objects.all(),
                PrintMediaMaterial.objects.all(),
                PrintMediaMaterial.objects.all()
            )
        )
