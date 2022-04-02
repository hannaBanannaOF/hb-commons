from .mixins import QueryStringParamSearchMixin
from rest_framework.generics import RetrieveAPIView
# Create your views here.

class QueryStringRetriveApiView(QueryStringParamSearchMixin, RetrieveAPIView):
    pass