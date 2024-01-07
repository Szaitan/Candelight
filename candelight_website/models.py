from django.db import models

# Create your models here.


class RealisationsType(models.Model):
    type = models.CharField(max_length=75)

    def __str__(self):
        return f"{self.type}"

    def delete(self, *args, **kwargs):
        products_products = RealisationsProject.objects.filter(category=self)
        for product in products_products:
            product.delete()

        super(RealisationsType, self).delete(*args, **kwargs)


class RealisationsProject(models.Model):
    object = models.CharField(max_length=75)
    arrangement = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75, unique=True)
    design_office = models.CharField(max_length=75, blank=True)
    photo = models.CharField(max_length=120, blank=True)
    category = models.ForeignKey(RealisationsType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="realisations_images", null=True)

    def delete(self, *args, **kwargs):
        # Main image from RealisationProject
        storage, path = self.image.storage, self.image.path
        storage.delete(path)

        # Additional images for Realisation Project
        additional_images = RealisationsPhotos.objects.filter(main_object=self)
        for additional_image in additional_images:
            additional_image.delete()

        super(RealisationsProject, self).delete(*args, **kwargs)

    def __str__(self):
        return f"{self.object} {self.category}"


class RealisationsPhotos(models.Model):
    main_object = models.ForeignKey(RealisationsProject, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="realisations_additional_images")

    def delete(self, *args, **kwargs):
        storage, path = self.photo.storage, self.photo.path
        storage.delete(path)
        super(RealisationsPhotos, self).delete(*args, **kwargs)

    def __str__(self):
        return f"{self.main_object}"


class ProductsInternalExternal(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

    def delete(self, *args, **kwargs):
        # Delete related ProductsProduct images
        products_subgroup = ProductsSubgroup.objects.filter(main_group=self)
        for product in products_subgroup:
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
