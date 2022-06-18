from django.db import models


class Order(models.Model):
    order_number = models.BigIntegerField(
        verbose_name='Номер заказа',
    )
    usd_price = models.DecimalField(
        verbose_name='Стоимость, $',
        max_digits=15,
        decimal_places=2,
    )
    rur_price = models.DecimalField(
        verbose_name='Стоимость, руб',
        max_digits=15,
        decimal_places=2,
    )
    delivery_date = models.DateField()
    created_at = models.DateTimeField(
        verbose_name='создан',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='обновлен',
        auto_now=True,
    )

    class Meta:
        db_table = 'orders'
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'{self.order_number} - {self.delivery_date}'
