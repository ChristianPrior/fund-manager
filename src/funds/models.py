from django.db import models
from django.utils.translation import gettext_lazy as _


class Fund(models.Model):
    class Currencies(models.TextChoices):
        USD = "USD", _("USD")

    class Strategies(models.TextChoices):
        ARBITRAGE = "Arbitrage", _("Arbitrage")
        LONG_SHORT_EQUITY = "Long/Short Equity", _("Long/Short Equity")
        GLOBAL_MACRO = "Global Macro", _("Global Macro")

    name = models.CharField(unique=True, max_length=200)
    strategy = models.CharField(choices=Strategies, max_length=100)
    aum = models.PositiveIntegerField(blank=True, null=True)
    currency_code = models.CharField(choices=Currencies, default="USD", max_length=3)
    inception_date = models.DateField(blank=True, null=True)
