# Generated by Django 3.1.3 on 2024-03-07 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20240307_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profession',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='', max_length=20, null=True),
        ),
    ]