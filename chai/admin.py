from django.contrib import admin
from .models import chaivariety, chaicertificate, chaiReview, store

# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model = chaiReview
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_added', 'type')
    inlines = [ChaiReviewInline]

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_no', 'certificate')

class storeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_variety',)

admin.site.register(chaivariety, ChaiVarietyAdmin)
admin.site.register(store, storeAdmin)
admin.site.register(chaicertificate, ChaiCertificateAdmin)
