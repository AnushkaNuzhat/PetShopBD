from django.db import models
from django.urls import reverse
import datetime
# Create your models here.

# class Store(models.Model):
#     store_id = models.IntegerField(primary_key = True)
#     store_name = models.CharField(max_length = 50)
#     location = models.CharField(max_length = 50)
#     city = models.CharField(max_length=50)

#     def __str__(self):
#         return self.store_name


# class Staff(models.Model):
#     staff_id = models.IntegerField(primary_key = True)
#     name = models.CharField(max_length = 50)
#     age = models.IntegerField()
#     gender_choice = (
#         ("male", "Male"),
#         ("female", "Female"),
#         ("other","Other")
#     )
#     gender = models.CharField(choices = gender_choice, max_length = 50)
#     adress= models.CharField(max_length = 50)
#     phone_no = models.CharField(max_length=15)
#     salary = models.IntegerField()
#     join_date = models.DateField()
#     store = models.ForeignKey(Store, on_delete = models.CASCADE)

#     def __str__(self):
#         return f'{self.name} -- {self.store}'

# class Supplier(models.Model):
#     supplier_id = models.IntegerField(primary_key = True)
#     name = models.CharField(max_length = 50)
#     email = models.EmailField(unique= True)
#     street = models.CharField(max_length = 50)
#     city = models.CharField(max_length = 50)
#     country = models.CharField(max_length = 50)

#     def __str__(self):
#         return f'{self.name}'


# class Customer(models.Model):
#     customer_id = models.IntegerField(primary_key = True)
#     name = models.CharField(max_length= 50)
#     phone_no = models.CharField(max_length = 15)
#     email = models.EmailField(unique= True)

#     def __str__(self):
#         return self.name

# class Veterinarians(models.Model):
#     veterinarians_id = models.IntegerField(primary_key = True)
#     name = models.CharField(max_length = 50)
#     email = models.EmailField(unique= True)
#     salary = models.IntegerField()
#     store_id = models.ForeignKey(Store, on_delete = models.CASCADE)
#     hire_date = models.DateField()

#     def __str__(self):
#         return f'{self.name}'

#     class Meta:
#         verbose_name = 'Veterinary'
#         verbose_name_plural = 'Veterinaries'

class Category(models.Model):
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Pet(models.Model):
    main_image = models.ImageField(upload_to='pets')
    name = models.CharField(max_length=264)
    gender = models.CharField(max_length=20, default='male')
    breed = models.CharField(max_length=264, default='')
    dob = models.DateField(default=datetime.date.today)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category")
    preview_text = models.TextField(
        max_length=200, verbose_name="preview_text")
    detail_text = models.TextField(max_length=1000, verbose_name="description")
    price = models.FloatField(default=0.00)
    old_price = models.FloatField(default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at', ]
        verbose_name_plural = "Pets"


# class Shipment(models.Model):
#     class Meta:
#         unique_together = (('shipments_id', 'store_id','animal_id'))

#     shipments_id = models.IntegerField()
#     store_id = models.ForeignKey(Store, on_delete = models.CASCADE)
#     animal_id = models.ForeignKey(Animal_Details, on_delete = models.CASCADE)
#     qty = models.IntegerField()
#     buying_ppu = models.IntegerField()
#     supplier_id = models.ForeignKey(Supplier, on_delete = models.CASCADE)
#     date = models.DateField()

#     def __str__(self):
#         return f'{self.shipments_id}'

# class Inventory(models.Model):
#     p_id = models.AutoField(primary_key = True)
#     shipment_id = models.ForeignKey(Shipment, on_delete = models.CASCADE)
#     store_id = models.ForeignKey(Store, on_delete = models.CASCADE)
#     animal_id = models.ForeignKey(Animal_Details, on_delete = models.CASCADE)
#     qty = models.PositiveIntegerField()

#     def __str__(self):
#         return f'{self.p_id}'

# class Purchase(models.Model):
#       trx_id = models.AutoField(primary_key = True)
#       p_id = models.ForeignKey(Inventory, on_delete = models.CASCADE)
#       customer_id = models.ForeignKey(Customer, on_delete = models.CASCADE)
#       qty = models.IntegerField()
#       sellling_ppu = models.IntegerField()
#       p_date = models.DateField()

#       def __str__(self):
#         return f'{self.customer_id}'

# class Pet(models.Model):
#     pet_id = models.IntegerField(primary_key=True)
#     p_id = models.ForeignKey(Inventory, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     gender_choice = (
#         ("male", "Male"),
#         ("female", "Female"),
#         ("other","Other")
#     )
#     gender = models.CharField(choices = gender_choice, max_length = 50)
#     date_of_birth = models.DateField()

#     def __str__(self):
#         return f'{self.name}'

# class Diseased_Pet(models.Model):
#     sl_no = models.AutoField(primary_key=True)
#     pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE)
#     vet_id = models.ForeignKey(Veterinarians, on_delete=models.CASCADE)
#     deases_name = models.CharField(max_length=50)
#     date_of_disease = models.DateField(null=True)
#     def __str__(self):
#         return f'{self.pet_id} - {self.deases_name}'

#     class Meta:
#         verbose_name = 'Diseased Pet'
#         verbose_name_plural = 'Diseased Pets'

# class Treatment(models.Model):
#     class Meta:
#         unique_together = (('treatment_id', 'sl_no'))
#     sl_no = models.IntegerField()
#     treatment_id = models.ForeignKey(Diseased_Pet, on_delete=models.CASCADE)
#     date_of_treatment = models.DateField()
#     medicine = models.CharField(max_length=100)

#     def __str__(self):
#         return f'{self.treatment_id} - {self.medicine}'


class BannerImage(models.Model):
    image_name = models.CharField(max_length=100)
    banner_image = models.ImageField(
        upload_to='photos/banner_image', blank=True)
