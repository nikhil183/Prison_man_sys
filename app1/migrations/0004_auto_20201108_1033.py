# Generated by Django 2.2 on 2020-11-08 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20201108_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prisoner',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='prisoners'),
        ),
    ]
