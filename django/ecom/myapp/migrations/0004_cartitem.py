# Generated by Django 5.0.2 on 2024-04-20 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_products1_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('status', models.CharField(default='pending', max_length=100)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='myapp.buyer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='myapp.products1')),
            ],
            options={
                'verbose_name': 'Cart Item',
                'verbose_name_plural': 'Cart Items',
                'unique_together': {('buyer', 'product')},
            },
        ),
    ]