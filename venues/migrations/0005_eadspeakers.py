# Generated by Django 4.2.5 on 2024-09-28 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0004_eadcities_eadvenue_delete_venue'),
    ]

    operations = [
        migrations.CreateModel(
            name='EADSpeakers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('designition', models.CharField(max_length=50)),
                ('linkedin', models.URLField()),
                ('photo', models.ImageField(upload_to='EAD/images')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.eadcities')),
            ],
        ),
    ]
