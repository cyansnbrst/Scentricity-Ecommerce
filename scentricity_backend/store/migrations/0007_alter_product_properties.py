# Generated by Django 4.2.7 on 2024-04-03 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_productproperty_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='properties',
            field=models.ManyToManyField(blank=True, through='store.ProductProperty', to='store.property'),
        ),
    ]