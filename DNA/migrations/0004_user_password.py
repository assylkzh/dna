# Generated by Django 4.2.6 on 2023-10-26 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DNA', '0003_remove_basket_cost_remove_basket_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='0000', max_length=50),
        ),
    ]
