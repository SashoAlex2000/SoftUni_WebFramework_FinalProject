# Generated by Django 4.1.4 on 2022-12-10 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='isCompany',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]