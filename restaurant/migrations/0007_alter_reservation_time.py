# Generated by Django 5.0.7 on 2024-11-29 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_rename_subjet_message_subject_alter_reservation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.CharField(max_length=50),
        ),
    ]
