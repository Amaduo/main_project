# Generated by Django 5.0.7 on 2024-11-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('subjet', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
