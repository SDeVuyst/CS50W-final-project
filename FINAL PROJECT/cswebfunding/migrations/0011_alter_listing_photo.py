# Generated by Django 3.2.5 on 2021-08-01 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cswebfunding', '0010_alter_listing_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='static/uploads'),
        ),
    ]
