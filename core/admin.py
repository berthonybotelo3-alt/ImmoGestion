from django.contrib import admin
from .models import Property, PropertyImage, Reservation, User

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 0  # Pas de lignes vides par défaut, l'admin ajoute ce dont il a besoin

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'property_type', 'price', 'status', 'created_at')
    list_filter = ('status', 'property_type')
    search_fields = ('title', 'address', 'owner__username')
    list_editable = ('status',)  # Permet de changer le statut directement depuis la liste
    inlines = [PropertyImageInline]
    readonly_fields = ('created_at',)

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'image')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('property', 'client', 'action_type', 'date_period', 'created_at')
    list_filter = ('action_type',)
    search_fields = ('property__title', 'client__username')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    list_filter = ('role',)
    search_fields = ('username', 'email')

