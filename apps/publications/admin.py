from django.contrib import admin

from .models import Comment, Event, Publication


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}

    # Read-only fields
    readonly_fields = ("created_at", "updated_at")


class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created_at")
    list_filter = ("status", "is_blog_post", "is_news", "is_featured", "allow_comments")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}

    fieldsets = (
        ("Publication Details", {"fields": ("title", "slug", "content", "preview", "author")}),
        (
            "Publication Options",
            {"fields": ("status", "published_at", "is_blog_post", "is_news", "is_featured", "allow_comments", "keywords")},
        ),
    )

    # Read-only fields
    readonly_fields = ("created_at", "updated_at")

    def get_form(self, request, obj=None, **kwargs):
        # Overriden to prepopulate the author field with the current user
        form = super().get_form(request, obj, **kwargs)
        if not obj:  # Only prepopulate for new publications
            form.base_fields["author"].initial = request.user
        return form


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author_name", "author_email", "is_approved", "created_at")
    search_fields = ["author_name", "author_email", "content"]
    list_filter = ["created_at", "is_approved"]


admin.site.register(Event, EventAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Comment, CommentAdmin)
