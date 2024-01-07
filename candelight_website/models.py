from django.db import models

# Create your models here.


class RealisationsType(models.Model):
    type = models.CharField(max_length=75)

    def __str__(self):
        return f"{self.type}"


class RealisationsProject(models.Model):
    arrangement = models.CharField(max_length=75)
    object = models.CharField(max_length=75)
    design_office = models.CharField(max_length=75)
    photo = models.CharField(max_length=120)
    category = models.ForeignKey(RealisationsType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="realisations_images", null=True)

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        storage.delete(path)
        super(RealisationsProject, self).delete(*args, **kwargs)

    def __str__(self):
        return f"{self.title} {self.category}"


class RealisationsPhotos(models.Model):
    main_object = models.ForeignKey(RealisationsProject, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="realisations_additional_images")

    def delete(self, *args, **kwargs):
        storage, path = self.photo.storage, self.photo.path
        storage.delete(path)
        super(RealisationsPhotos, self).delete(*args, **kwargs)

    def __str__(self):
        return f"{self.title} {self.category}"


class ProductsInternalExternal(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

    def delete(self, *args, **kwargs):
        # Delete related ProductsProduct images
        products_products = ProductsProduct.objects.filter(sub_group=self)
        for product in products_products:
            product.delete()

        super(ProductsInternalExternal, self).delete(*args, **kwargs)


class ProductsSubgroup(models.Model):
    name = models.CharField(max_length=100)
    main_group = models.ForeignKey(ProductsInternalExternal, on_delete=models.CASCADE, null=True)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

    def delete(self, *args, **kwargs):
        # Delete related ProductsProduct images
        products_products = ProductsProduct.objects.filter(sub_group=self)
        for product in products_products:
            product.delete()

        super(ProductsSubgroup, self).delete(*args, **kwargs)


class ProductsProduct(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    main_group = models.ForeignKey(ProductsInternalExternal, on_delete=models.CASCADE)
    sub_group = models.ForeignKey(ProductsSubgroup, on_delete=models.CASCADE, null=True)
    main_image = models.ImageField(upload_to="products_images", null=True)

    def delete(self, *args, **kwargs):
        storage, path = self.main_image.storage, self.main_image.path
        storage.delete(path)
        super(ProductsProduct, self).delete(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.main_group} {self.sub_group}"
