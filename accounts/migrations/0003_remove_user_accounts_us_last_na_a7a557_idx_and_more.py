# Generated by Django 4.0.6 on 2023-08-23 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_staff'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='user',
            name='accounts_us_last_na_a7a557_idx',
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['last_name', 'first_name'], name='accounts_us_last_na_ddbf2c_idx'),
        ),
    ]
