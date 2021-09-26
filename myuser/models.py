from django.db import models
import os


def user_directory_path(instance, filename):
    ext = filename.split('.').pop()
    filename = '{0}{1}.{2}'.format(instance.name, instance.identity_card, ext)
    return os.path.join(instance.major.name, filename)


class myuser_model(models.Model):
    head = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    name = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=128, blank=False)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    sex = models.IntegerField()
    state = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def photo_url(self):
        if self.head and hasattr(self.head, 'url'):
            return self.head.url
        else:
            return '/media/default/user.jpg'

    class Meta:
        ordering = ['created']


class ware(models.Model):
    name = models.CharField(max_length=100, blank=False)
    price = models.IntegerField()
    cost = models.IntegerField()
    location = models.CharField(max_length=128, default='BeiJing')


class warehouse(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=128, blank=True)
    wares = models.ManyToManyField(ware, through='amount_model')


class amount_model(models.Model):
    ware = models.ForeignKey(ware, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    operation = models.IntegerField(default=0)


class order_table_model(models.Model):
    buyer_name = models.CharField(max_length=100, blank=True)
    buyer_phone_number = models.CharField(max_length=20, blank=True)
    buyer_email = models.EmailField(blank=True)
    buyer_sex = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)


class order_model(models.Model):
    order_table = models.ForeignKey(order_table_model, on_delete=models.CASCADE)
    ware = models.ForeignKey(ware, on_delete=models.CASCADE)
    number = models.IntegerField()


class buyer_model(models.Model):
    buyer_name = models.CharField(max_length=100, blank=True)
    buyer_phone_number = models.CharField(max_length=20, blank=True)
    buyer_email = models.EmailField(blank=True)
    buyer_sex = models.IntegerField(default=0)