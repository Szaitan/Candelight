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


class ProductsProduct(models.Model):
    name = models.CharField(max_length=200)
    group = models.ForeignKey(ProductsInternalExternal, on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to="products_images", null=True)

    def delete(self, *args, **kwargs):
        storage, path = self.main_image.storage, self.main_image.path
        storage.delete(path)
        super(ProductsProduct, self).delete(*args, **kwargs)

    def __str__(self):
        return f"{self.group} {self.name}"
