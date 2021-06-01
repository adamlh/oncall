from rest_framework.generics import ListAPIView

from .serializers import ListSerializer
from .models import Members, DateActive


class ListApi(ListAPIView):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer

class DatesApi(ListAPIView):
    queryset = DateActive.objects.all()
    serializer_class = DatesSerializer