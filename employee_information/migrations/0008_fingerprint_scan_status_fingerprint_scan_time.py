# Generated by Django 5.0.4 on 2024-04-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0007_fingerprint_delete_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='fingerprint',
            name='scan_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fingerprint',
            name='scan_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
