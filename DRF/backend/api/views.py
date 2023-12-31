
from products.models import Product
from products.serializers import ProductSerializer

from django.forms.models import model_to_dict
from rest_framework.response import Response


from rest_framework.decorators import api_view


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF api view
    """

    serializer = ProductSerializer(data=request.data)
    data = {}
    if serializer.is_valid(raise_exception=True):
        print (serializer.data)
        return Response(serializer.data)
    return Response({"invalid":"not good data"}, status=400)

