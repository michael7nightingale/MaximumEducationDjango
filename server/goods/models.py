from django.db import models
from uuid import uuid4
from slugify import slugify


def generate_uuid() -> str:
    return str(uuid4())


class UUIDSlugModel(models.Model):
    """Abstract model for auto-slug field."""
    id = models.CharField(primary_key=True, max_length=255, default=generate_uuid)
    slug = models.SlugField(unique=True, db_index=True, blank=True)

    objects = models.Manager()

    def save(self, **kwargs):
        """Method to generate slug field."""
        field = getattr(self, self.SlugMeta.slug_on_field)
        self.slug = slugify(field)
        return super().save(**kwargs)

    class SlugMeta:
        slug_on_field: str

    class Meta:
        abstract = True


class Category(UUIDSlugModel):
    name = models.CharField(max_length=120, db_index=True, unique=True)

    def __str__(self):
        return self.name

    class SlugMeta:
        slug_on_field = "name"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Subcategory(UUIDSlugModel):
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="subcategories"
    )
    name = models.CharField(max_length=120, db_index=True, unique=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class SlugMeta:
        slug_on_field = "name"

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"


class CountryChoices(models.TextChoices):
    Russia = "RUSSIA", "Russia"
    China = "CHINA", "China"
    Korea = "KOREA", "Korea"


class Good(UUIDSlugModel):
    subcategory = models.ForeignKey(
        "Subcategory",
        on_delete=models.CASCADE,
        related_name="goods"
    )
    title = models.CharField(max_length=120, db_index=True)
    description = models.TextField()
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, null=True, blank=True)
    images = models.ManyToManyField(to="self", through="GoodImage")
    photo = models.ImageField(upload_to="goods_img/")
    made_in_country = models.CharField(max_length=100, choices=CountryChoices.choices, null=True, blank=True)
    amount = models.PositiveIntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    discount = models.PositiveIntegerField(null=True, blank=True)

    @property
    def available(self):
        return bool(self.amount)

    @property
    def total_price(self) -> float:
        if self.discount is None:
            return float(self.price)   # type: ignore
        return (1 - (self.discount/100)) * float(self.price)   # type: ignore

    class SlugMeta:
        slug_on_field = "title"

    class Meta:
        verbose_name = "Good"
        verbose_name_plural = "Goods"


class Brand(UUIDSlugModel):
    name = models.CharField(max_length=120, db_index=True, unique=True)
    description = models.TextField()
    country = models.CharField(max_length=100, choices=CountryChoices.choices)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class GoodImage(UUIDSlugModel):
    good = models.ForeignKey(
        "Good",
        on_delete=models.CASCADE
    )
    image = models.ImageField()

    objects = models.Manager()

    class Meta:
        verbose_name = "Good Image"
        verbose_name_plural = "Good Images"


class DescriptionItem(UUIDSlugModel):

    class DescriptionItemTagChoices(models.TextChoices):
        size = "SIZE", "Size"
        accumulator = "ACCUMUlATOR", "Accumulator"
        processor = "PROCESSOR", "processor"

    good = models.ForeignKey(
        "Good",
        on_delete=models.CASCADE,
        related_name="description_items"
    )
    key = models.CharField(max_length=70)
    value = models.CharField(max_length=100)
    tag = models.CharField(choices=DescriptionItemTagChoices.choices, max_length=100)

    objects = models.Manager()

    def __str__(self):
        return f"{self.key}: {self.value} ({self.tag})"

    class Meta:
        verbose_name = "Description Item"
        verbose_name_plural = "Description Items"
