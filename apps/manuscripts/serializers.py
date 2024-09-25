from rest_framework import serializers

from .models import ItemPart, HistoricalItemDescription


class ItemPartListSerializer(serializers.ModelSerializer):
    # Fields from HistoricalItem
    type = serializers.CharField(source="historical_item.type")
    format = serializers.CharField(source="historical_item.format")
    language = serializers.CharField(source="historical_item.language")
    vernacular = serializers.BooleanField(source="historical_item.vernacular")
    neumed = serializers.BooleanField(source="historical_item.neumed")
    hair_type = serializers.CharField(source="historical_item.hair_type")
    date = serializers.CharField(source="historical_item.date")
    date_sort = serializers.CharField(source="historical_item.date_sort")
    issuer = serializers.CharField(source="historical_item.issuer")
    named_beneficiary = serializers.CharField(source="historical_item.named_beneficiary")

    # Fields from CurrentItem
    repository_id = serializers.IntegerField(source="current_item.repository_id")
    shelfmark = serializers.CharField(source="current_item.shelfmark")

    class Meta:
        model = ItemPart
        fields = [
            "id",
            "type",
            "format",
            "language",
            "vernacular",
            "neumed",
            "hair_type",
            "date",
            "date_sort",
            "issuer",
            "named_beneficiary",
            "repository_id",
            "shelfmark",
        ]


class HistoricalItemDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalItemDescription
        fields = ["source", "content"]
