from django_filters import FilterSet
from .models import ItemPart


class ItemPartFilter(FilterSet):
    class Meta:
        model = ItemPart
        fields = {
            "historical_item__item_id": ["exact"],
            "current_item__item_id": ["exact"],
        }
