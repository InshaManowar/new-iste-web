# Generated by Django 3.0.2 on 2020-04-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20200407_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='Posters'),
        ),
        migrations.AlterField(
            model_name='event_date',
            name='end_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
