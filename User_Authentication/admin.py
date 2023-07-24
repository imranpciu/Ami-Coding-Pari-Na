from django.contrib import admin
from .models import KhojInputValue

class KhojInputValueAdmin(admin.ModelAdmin):
    list_display = ('user', 'input_values', 'timestamp')
    search_fields = ('user__username', 'input_values')
    list_filter = ('user', 'timestamp')

# Register the KhojInputValue model with the custom admin class
admin.site.register(KhojInputValue, KhojInputValueAdmin)
