# Generated by Django 3.0.6 on 2020-05-21 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='branch_postal_code',
            field=models.IntegerField(blank=True, default=44600, null=True),
        ),
    ]
