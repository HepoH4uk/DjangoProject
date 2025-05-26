from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="Фото продукта",
        help_text="Прикрепите фото продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        help_text="Введите категорию продукта",
        blank=True,
        null=True,
        related_name="products"
    )
    purchase_price = models.IntegerField(
        verbose_name="Цена продукта",
        help_text="Введите цену продукта"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "name",
            "category",
        ]

    def __str__(self):
        return self.name

