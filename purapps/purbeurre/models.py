"""Models module."""

from django.db import models
from django.db.models import Count
from django.conf import settings
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class Nutriscore(models.Model):
    """Create nutriscore table."""

    type = models.CharField(max_length=1, unique=True)

    def __str__(self) -> str:
        """Return str representation."""
        return f"{self.id} - {self.type}"


class Category(models.Model):
    """Create category table."""

    name = models.CharField(max_length=120, unique=True, default=False)

    def __str__(self) -> str:
        """Return str representation."""
        return f"{self.id} - {self.name}"

    @classmethod
    def find_best_category(cls):
        """Find the best category."""


class Product(models.Model):
    """Create product table."""

    name = models.CharField(max_length=240, unique=True, default=False, blank=True)
    brand = models.CharField(max_length=180, default=False, blank=True)
    image = models.URLField(max_length=255, default=False, blank=True, null=True)
    nutriments = models.JSONField()
    url = models.CharField(max_length=255, unique=True, default=False, blank=True)
    categories = models.ManyToManyField(Category, related_name="category_owner")
    nutriscore = models.ForeignKey(Nutriscore, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Return str representation."""
        return f"{self.id} - {self.name} - {self.brand} - {self.url}\
 - {self.nutriscore} - {self.image} - {self.nutriments}"

    def find_substitute(self):
        """Find a substitute."""
        categories_id = self.categories.values("id")
        sorted_categories = (
            Product.objects.filter(categories__in=categories_id)
            .values("categories__id")
            .annotate(tot=Count("id", distinct=True))
            .order_by("tot")
        )
        if len(sorted_categories) > 1:
            offset = 0
            substitute = None

            while not substitute:
                best_cat = sorted_categories[offset].get("categories__id")
                substitute = Product.objects.filter(
                    categories__id=best_cat,
                    nutriscore__type__lt=self.nutriscore.type,
                ).order_by("nutriscore__type")

                offset += 1
                if self.nutriscore.type > "b":
                    offset_limit = 3
                offset_limit = 2
                if offset == offset_limit and not substitute:
                    return None
            return substitute


class SubstitutesManager(models.Manager):
    """SubstitutesManager class."""

    def create_substitute(self, user, product, reference):
        """Create substitute."""
        substitute = self.create(user_id=user, product=product, reference=reference)
        return substitute


class Substitutes(models.Model):
    """Create substitutes table."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="user_id",
        default=False,
        blank=True,
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        Product, related_name="product", default="", on_delete=models.CASCADE
    )
    reference = models.ForeignKey(
        Product, related_name="reference", default="", on_delete=models.CASCADE
    )

    objects = SubstitutesManager()

    def __str__(self) -> str:
        """Return str representation."""
        return f"{self.user} - {self.product} - {self.reference}"

    def save_sub(self, prod_inst, ref_product, user):
        """Save substitute in favorites."""
        substitute = Substitutes.objects.create_substitute(user, prod_inst, ref_product)
        return substitute

    def delete_sub(self, product_sel, ref_product_id, status):
        """Delete substitute from favorites."""
        self.product_sel = product_sel
        self.ref_product = ref_product_id

        if not status:
            substitute = Substitutes.objects.get(
                product_id=int(self.product_sel),
                reference_id=self.ref_product.id,
                user_id=self.user.id,
            )
            substitute.delete()
        return status
