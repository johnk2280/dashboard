from django.db import models


class Order(models.Model):
    order_id = models.BigIntegerField(
        verbose_name='Номер заказа',
        primary_key=True,
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
        return f'Заказ № {self.order_id} - ' \
               f'дата поставки: {self.delivery_date}'
