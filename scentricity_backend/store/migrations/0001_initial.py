# Generated by Django 4.2.7 on 2024-04-01 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название бренда')),
            ],
        ),
        migrations.CreateModel(
            name='Perfume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('quantity', models.IntegerField(default=0, verbose_name='Количество на складе')),
                ('volume', models.IntegerField(null=True, verbose_name='Объем')),
                ('type', models.CharField(choices=[('EDT', 'Eau de Toilette'), ('EDP', 'Eau de Parfum'), ('P', 'Parfum')], default='P', max_length=3, verbose_name='Тип парфюма')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.brand', verbose_name='Название бренда')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Diffuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('quantity', models.IntegerField(default=0, verbose_name='Количество на складе')),
                ('volume', models.IntegerField(null=True, verbose_name='Объем')),
                ('service_time', models.CharField(max_length=5, verbose_name='Время службы, мес')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.brand', verbose_name='Название бренда')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Candle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('quantity', models.IntegerField(default=0, verbose_name='Количество на складе')),
                ('volume', models.IntegerField(null=True, verbose_name='Объем')),
                ('burning_time', models.IntegerField(verbose_name='Время горения, ч')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.brand', verbose_name='Название бренда')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
