# Generated by Django 2.1.7 on 2019-08-07 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ports', '0007_alter_field_clt_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='cxx_stdlib',
            field=models.CharField(default='', max_length=20),
        ),
    ]
