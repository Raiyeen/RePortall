# Generated by Django 5.2.1 on 2025-06-14 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RePortall', '0005_remove_customer_date_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportsubmission',
            old_name='Customer',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='reportsubmission',
            old_name='Review',
            new_name='review',
        ),
    ]
