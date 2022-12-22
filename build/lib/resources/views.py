import itertools

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import generic

from resources.models import (AudioVisualMaterial, Author, InformationMaterial, PrintMediaMaterial, SerialMaterial)

# Create your views here.

hashmap = {
    "Author": Author,
    "InformationMaterial": InformationMaterial,
    "AudioVisualMaterial": AudioVisualMaterial,
    "PrintMediaMaterial": PrintMediaMaterial,
    "SerialMaterial": SerialMaterial,
}


def get_stock_count(request, resource_type: str, resource_id: str):
    result = ""
    try:
        result = hashmap[resource_type].objects.get(id=int(resource_id))
    except Exception as e:
        print(e)
    return JsonResponse(
        {
            "stock_count": result.quantity if result else "N/A",
            "cost_per_unit": result.price_per_unit if result else "N/A",
        },
        safe=False
    )


class InventoryListView(generic.ListView, LoginRequiredMixin):
    context_object_name = "resources"
    template_name = "inventory/inventory_list_view.html"
    paginate_by = 40

    def get_queryset(self):
        return list(
            itertools.chain(
                PrintMediaMaterial.objects.all(),
                PrintMediaMaterial.objects.all(),
                AudioVisualMaterial.objects.all(),
            )
        )
