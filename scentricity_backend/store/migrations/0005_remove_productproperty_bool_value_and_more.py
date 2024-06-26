# Generated by Django 4.2.7 on 2024-04-02 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_productproperty_float_value_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productproperty',
            name='bool_value',
        ),
        migrations.RemoveField(
            model_name='productproperty',
            name='integer_value',
        ),
        migrations.RemoveField(
            model_name='productproperty',
            name='string_value',
        ),
        migrations.AddField(
            model_name='productproperty',
            name='value',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
