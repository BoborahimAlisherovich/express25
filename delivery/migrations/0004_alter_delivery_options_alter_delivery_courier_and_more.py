# Generated by Django 5.1.2 on 2024-12-04 11:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_alter_delivery_delivered_at_alter_review_comment'),
        ('order', '0002_alter_productorder_options_alter_order_courier_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'ordering': ['-delivery_time'], 'verbose_name': 'Delivery', 'verbose_name_plural': 'Deliveries'},
        ),
        migrations.AlterField(
            model_name='delivery',
            name='courier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliveries', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='delivery', to='order.order'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterModelTable(
            name='delivery',
            table=None,
        ),
        migrations.AlterModelTable(
            name='review',
            table=None,
        ),
    ]