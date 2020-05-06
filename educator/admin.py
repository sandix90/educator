from constance.admin import ConstanceForm, ConstanceAdmin, Config
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin

from educator.models import Feedback, Page


class ConstanceConfigForm(ConstanceForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['INDEX_TEXT'].widget = CKEditorWidget()


class ConfigAdmin(ConstanceAdmin):
    change_list_form = ConstanceConfigForm


admin.site.unregister([Config])
admin.site.register([Config], ConfigAdmin)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'sender_name', 'email', 'text')
    list_display_links = ('created_at',)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'title', 'display')
    list_display_links = ('title',)
    prepopulated_fields = {"slug": ("title",)}
