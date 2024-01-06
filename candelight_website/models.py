from django.db import models

# Create your models here.


class RealisationsType(models.Model):
    type = models.CharField(max_length=75)

    def __str__(self):
        return f"{self.type}"


class RealisationsProject(models.Model):
    title = models.CharField(max_length=75)
    category = models.ForeignKey(RealisationsType, on_delete=models.CASCADE)
    description = models.TextField(max_length=450)
    image = models.ImageField(upload_to="realisations_images", null=True)

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        storage.delete(path)
        super(RealisationsProject, self).delete(*args, **kwargs)

    def __str__(self):
        return f"{self.title} {self.category}"


class ProductsInternalExternal(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class ProductsSubgroup(models.Model):
    name = models.CharField(max_length=100)
    main_group = models.ForeignKey(ProductsInternalExternal, on_delete=models.CASCADE, null=True)
    number = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


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
