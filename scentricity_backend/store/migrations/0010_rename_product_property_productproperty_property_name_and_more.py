# Generated by Django 4.2.7 on 2024-04-03 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_productproperty_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productproperty',
            old_name='product_property',
            new_name='property_name',
        ),
        migrations.AlterField(
            model_name='productproperty',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='store.product'),
        ),
    ]
