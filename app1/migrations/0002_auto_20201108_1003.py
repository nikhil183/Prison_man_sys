# Generated by Django 2.2 on 2020-11-08 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prisoner',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='prisoner',
            name='case',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='prisoner',
            name='gender',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='prisoner',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='prisoner',
            name='state',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='prisoner',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
