# Generated by Django 4.2.7 on 2024-04-01 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('quantity', models.IntegerField(default=0, verbose_name='Количество на складе')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.brand', verbose_name='Название бренда')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='ProductProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string_value', models.CharField(blank=True, max_length=255, null=True)),
                ('integer_value', models.IntegerField(blank=True, null=True)),
                ('float_value', models.FloatField(blank=True, null=True)),
                ('choice_value', models.CharField(blank=True, max_length=50, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название свойства')),
                ('property_type', models.CharField(choices=[('string', 'String'), ('integer', 'Integer'), ('float', 'Float'), ('choice', 'Choice')], default='string', max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='diffuser',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='perfume',
            name='brand',
        ),
        migrations.DeleteModel(
            name='Candle',
        ),
        migrations.DeleteModel(
            name='Diffuser',
        ),
        migrations.DeleteModel(
            name='Perfume',
        ),
        migrations.AddField(
            model_name='productproperty',
            name='product_property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.property'),
        ),
        migrations.AddField(
            model_name='product',
            name='properties',
            field=models.ManyToManyField(blank=True, through='store.ProductProperty', to='store.property', verbose_name='Свойства'),
        ),
    ]
