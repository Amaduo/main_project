# Generated by Django 5.0.7 on 2024-12-02 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_alter_reservation_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]
