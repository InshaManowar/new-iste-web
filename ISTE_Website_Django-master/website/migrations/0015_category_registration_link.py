# Generated by Django 3.0.5 on 2020-09-17 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20200720_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='registration_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
