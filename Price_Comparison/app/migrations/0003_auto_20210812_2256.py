# Generated by Django 3.2.6 on 2021-08-12 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_specifications_screen_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Availability',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.availability'),
        ),
        migrations.AlterField(
            model_name='product',
            name='BatteryCapacity',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.batterycapacity'),
        ),
        migrations.AlterField(
            model_name='product',
            name='FrontCamera',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.frontcamera'),
        ),
        migrations.AlterField(
            model_name='product',
            name='InternalStorage',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.internalstorage'),
        ),
        migrations.AlterField(
            model_name='product',
            name='NetworkConnectivity',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.networkconnectivity'),
        ),
        migrations.AlterField(
            model_name='product',
            name='NumberOfCores',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.numberofcores'),
        ),
        migrations.AlterField(
            model_name='product',
            name='OperatingSystem',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.operatingsystem'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PrimaryRearCamera',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.primaryrearcamera'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProcessorSpeed',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.processorspeed'),
        ),
        migrations.AlterField(
            model_name='product',
            name='RAM',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.ram'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ScreenSize',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.screensize'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
    ]
