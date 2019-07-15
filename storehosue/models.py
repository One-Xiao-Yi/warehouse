from django.db import models


class Suppliers(models.Model):
    supplier_id = models.CharField(primary_key=True, max_length=45)
    supplier_name = models.CharField(max_length=45, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suppliers'


class Goods(models.Model):
    good_id = models.CharField(primary_key=True, max_length=45)
    good_name = models.CharField(max_length=45, blank=True, null=True)
    # supplier_id = models.CharField(max_length=45, blank=True, null=True)
    purchase_price = models.IntegerField(blank=True, null=True)
    accumulate = models.IntegerField(blank=True, null=True)
    supplier = models.OneToOneField(to=Suppliers, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'goods'


class Stock(models.Model):
    stock_id = models.CharField(primary_key=True, max_length=45)
    # good_id = models.CharField(max_length=45, blank=True, null=True)
    retail_price = models.IntegerField(blank=True, null=True)
    surplus = models.IntegerField(blank=True, null=True)
    date_of_manufacture = models.DateField(blank=True, null=True)
    quality_gurantee_period = models.IntegerField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    good = models.OneToOneField(to=Goods, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'stock'
