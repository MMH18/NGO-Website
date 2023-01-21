from django.contrib import admin
from products.models import contact,contacts

# Register your models here.


@admin.register(contacts)
class contactsAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','email','city']
    list_display_links=['firstname']
    list_filter=['firstname','lastname','city']
    list_per_page= 24
    search_fields = ['firstname', 'lastname', 'city']

@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ['firstname1','lastname1','email','city']
    list_display_links=['firstname1']
    list_filter=['firstname1','lastname1','city']
    list_per_page= 24
    search_fields = ['firstname1', 'lastname1', 'city']

