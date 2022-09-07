from django.contrib import admin
from .models import (CustomMetaTag,MetaTag,Schema)
# Register your models here.


class CustomMetaTagInline(admin.TabularInline):
    model = CustomMetaTag
    extra: int = 1

@admin.register(MetaTag)
class MetaTagAdmin(admin.ModelAdmin):
    inlines = (CustomMetaTagInline,)

@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
    pass
