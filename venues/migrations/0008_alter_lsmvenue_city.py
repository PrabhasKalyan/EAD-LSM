# Generated by Django 4.2.5 on 2024-09-28 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0007_alter_lsmspeakers_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lsmvenue',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.lsmcities'),
        ),
    ]
