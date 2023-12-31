# Generated by Django 4.2.6 on 2023-10-26 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DNA', '0002_cold_cost_cold_image_dessert_cost_dessert_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='image',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='image',
        ),
        migrations.RemoveField(
            model_name='types',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='types',
            name='image',
        ),
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
        migrations.AlterField(
            model_name='basket',
            name='basket_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='item_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='types',
            name='type_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
