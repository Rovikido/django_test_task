from django.views.generic import ListView

import core.models as md


class ProductListView(ListView):
    model = md.Product
    template_name = 'product_list.html'
    context_object_name = 'products'
