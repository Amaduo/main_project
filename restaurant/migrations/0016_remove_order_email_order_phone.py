# Generated by Django 5.0.7 on 2024-12-04 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0015_order_delete_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.IntegerField(default='0796830208'),
        ),
    ]
