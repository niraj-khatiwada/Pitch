# Generated by Django 3.0.6 on 2020-05-21 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0005_auto_20200521_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='mAddress',
        ),
        migrations.AlterField(
            model_name='branch',
            name='postal_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
