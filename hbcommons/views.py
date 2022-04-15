from .mixins import QueryStringParamSearchMixin
from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from .serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
@login_required
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class QueryStringRetriveApiView(QueryStringParamSearchMixin, RetrieveAPIView):
    pass