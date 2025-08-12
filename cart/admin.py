from django.contrib import admin
from . import models


class OrderItemAdmin(admin.TabularInline):
    model = models.OrderItem



    

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'is_paid', 'status')
    inlines = (OrderItemAdmin,)
    list_filter = ('is_paid', 'status')
    search_fields = ('tracking_code',)



admin.site.register(models.Account)





