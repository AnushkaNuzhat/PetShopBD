from django.contrib import admin
from .models import *
# Register your models here.

# class StoreAdmin(admin.ModelAdmin):
#     list_display = ('store_name','location','city')

# admin.site.register(Store, StoreAdmin)


# class StaffAdmin(admin.ModelAdmin):
#     list_display = ('name', 'phone_no','gender','store')
# admin.site.register(Staff, StaffAdmin)


# class SuplierAdmin(admin.ModelAdmin):
#     list_display = ('name','email','city', 'country',)
# admin.site.register(Supplier, SuplierAdmin)

# class CustomersAdmin(admin.ModelAdmin):
#     list_display = ('name','phone_no','email',)

# admin.site.register(Customer, CustomersAdmin)


# class VeterinariansAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'salary', 'store_id', 'hire_date',)
# admin.site.register(Veterinarians, VeterinariansAdmin)

# class AnimalCategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug':('animal_cat',)}
#     list_display = ('animal_cat',)
# admin.site.register(AnimalCategory, AnimalCategoryAdmin)


# class Animal_DetailsAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug':('animal_type','breed',)}
#     list_display = ('animal_type', 'breed','animal_image',)
# admin.site.register(Animal_Details, Animal_DetailsAdmin)


# class ShipmentsAdmin(admin.ModelAdmin):
#     list_display = ('supplier_id','store_id', 'animal_id', 'qty', 'buying_ppu','date',)
# admin.site.register(Shipment, ShipmentsAdmin)

# class InventoryAdmin(admin.ModelAdmin):
#     list_display = ('shipment_id', 'store_id', 'animal_id', 'qty')
# admin.site.register(Inventory, InventoryAdmin)


# class PurchaseAdmin(admin.ModelAdmin):
#     list_display = ('p_id', 'customer_id','qty','sellling_ppu','p_date')
# admin.site.register(Purchase, PurchaseAdmin)


# class PetAdmin(admin.ModelAdmin):
#     list_display = ('pet_id', 'p_id', 'name', 'gender', 'date_of_birth')
# admin.site.register(Pet, PetAdmin)

# class Diseased_PetAdmin(admin.ModelAdmin):
#     list_display = ('pet_id', 'vet_id', 'deases_name')
# admin.site.register(Diseased_Pet, Diseased_PetAdmin)


# class TreatmentAdmin(admin.ModelAdmin):
#     list_display = ('treatment_id', 'date_of_treatment', 'medicine')
# admin.site.register(Treatment, TreatmentAdmin)

admin.site.register(Category)
admin.site.register(Pet)


class BannerImageAdmin(admin.ModelAdmin):
    list_display = ['image_name', 'banner_image']


admin.site.register(BannerImage, BannerImageAdmin)
