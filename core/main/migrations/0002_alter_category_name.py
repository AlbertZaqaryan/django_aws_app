# Generated by Django 5.0.3 on 2024-03-20 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default=None, max_length=30, verbose_name='Caregory name'),
        ),
    ]
