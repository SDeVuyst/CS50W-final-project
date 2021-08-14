# Generated by Django 3.2.5 on 2021-08-14 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cswebfunding', '0025_listing_popularity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cswebfunding.listing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
