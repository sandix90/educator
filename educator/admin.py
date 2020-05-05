from constance.admin import ConstanceForm, ConstanceAdmin, Config
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin


class ConstanceConfigForm(ConstanceForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['INDEX_TEXT'].widget = CKEditorWidget()
        self.fields['ABOUT_US'].widget = CKEditorWidget()


class ConfigAdmin(ConstanceAdmin):
    change_list_form = ConstanceConfigForm


admin.site.unregister([Config])
admin.site.register([Config], ConfigAdmin)
