# Generated by Django 3.2.5 on 2021-08-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cswebfunding', '0016_listing_donated'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='default-user.jpg', upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo',
            field=models.ImageField(default='default-listing.jpg', upload_to='media/'),
        ),
    ]