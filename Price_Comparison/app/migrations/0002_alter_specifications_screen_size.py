# Generated by Django 3.2.6 on 2021-08-12 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specifications',
            name='Screen_Size',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]