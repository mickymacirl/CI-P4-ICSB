from django.contrib import admin
from .models import Post, Comment

# class PostAdmin(SummernoteModelAdmin):
    # Fields to be rendered with the Summernote editor
#    summernote_fields = '__all__'

# The PostAdmin class inherits from ModelAdmin, and defines a list_display, list_filter,
# search_fields, and prepopulated_fields

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created_on',
                    'category', 'is_pinned', 'status', 'content',)
    list_filter = ("status", "author", "created_on", 'category', 'is_pinned',)
    search_fields = ['title', 'content', 'category', 'is_pinned',]
    prepopulated_fields = {'slug': ('title',)}

    # Add an action to mark posts as published
    def make_published(self, request, queryset):
        rows_updated = queryset.update(status='1')
        if rows_updated == 1:
            message_bit = "1 post was"
        else:
            message_bit = f"{rows_updated} posts were"
        self.message_user(request, f"{message_bit} successfully published!")
    make_published.short_description = "Set selected posts to published"

    # Add an action to mark posts as drafts
    def make_draft(self, request, queryset):
        rows_updated = queryset.update(status='0')
        if rows_updated == 1:
            message_bit = "1 post was"
        else:
            message_bit = f"{rows_updated} posts were"
        self.message_user(
            request, f"{message_bit} successfully marked as drafts.")
    make_draft.short_description = "Set selected posts to draft"

    # Add an action to mark posts as disabled
    def make_disabled(self, request, queryset):
        rows_updated = queryset.update(status='2')
        if rows_updated == 1:
            message_bit = "1 post was"
        else:
            message_bit = f"{rows_updated} posts were"
        self.message_user(
            request, f"{message_bit} successfully marked as disabled.")
    make_disabled.short_description = "Set selected posts as disabled"

    # Add a save and continue editing button on the edit form
    save_on_top = True
    save_as = True
    actions = ['make_published', 'make_draft', 'make_disabled']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active', 'status',)
    list_filter = ('active', 'created_on', 'name', 'post', 'status',)
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

    def mark_as_spam(self, request, queryset):
        queryset.update(status='spam')

    actions = ['approve_comments', 'mark_as_spam']

    def delete_comments(self, request, queryset):
        queryset.delete()

    def set_active(self, request, queryset):
        queryset.update(active=True)

    def set_inactive(self, request, queryset):
        queryset.update(active=False)

    actions = ['approve_comments', 'mark_as_spam',
               'delete_comments', 'set_active', 'set_inactive']


# Registering the Post model with the PostAdmin class.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
