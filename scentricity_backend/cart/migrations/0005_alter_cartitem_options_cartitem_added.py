# Generated by Django 4.2.7 on 2024-04-12 16:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_cart_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartitem',
            options={'ordering': ['-added']},
        ),
        migrations.AddField(
            model_name='cartitem',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]