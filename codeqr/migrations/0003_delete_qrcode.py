# Generated by Django 4.2.7 on 2024-06-16 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codeqr', '0002_rename_image_qrcode_codeqr'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QRCODE',
        ),
    ]
