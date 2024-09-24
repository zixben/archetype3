from rest_framework import serializers

from .models import Comment, Event, Publication


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "title", "created_at"]


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "title", "content", "created_at"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = "users.User"
        fields = ("id", "first_name", "last_name")


class PublicationListSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    number_of_comments = serializers.SerializerMethodField()

    def get_number_of_comments(self, publication):
        return publication.comments.filter(is_approved=True).count()

    class Meta:
        model = Publication
        fields = ["id", "title", "slug", "preview" "author", "number_of_comments", "published_at", "created_at"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["author_name", "content", "created_at"]


class PublicationDetailSerializer(PublicationListSerializer):
    author = UserSerializer()
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        approved_comments = Comment.objects.filter(post=obj, is_approved=True)
        return CommentSerializer(approved_comments, many=True).data

    class Meta:
        model = Publication
        fields = PublicationListSerializer.Meta.fields + ["content", "comments"]
