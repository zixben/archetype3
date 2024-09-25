from rest_framework.generics import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import ItemPart
from .serializers import ItemPartListSerializer

from .filters import ItemPartFilter


class ItemPartViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = ItemPart.objects.all()
    serializer_class = ItemPartListSerializer
    filterset_class = ItemPartFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related("historical_item", "current_item")
        return queryset

    @action(detail=True, methods=["get"])
    def historical_item_descriptions(self, request, *args, **kwargs):
        item_part = self.get_object()
        descriptions = item_part.historical_item.historicalitemdescription_set.all()
        return Response(HistoricalItemDescriptionSerializer(descriptions, many=True).data)
