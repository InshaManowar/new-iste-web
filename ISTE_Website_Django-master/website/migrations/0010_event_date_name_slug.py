# Generated by Django 3.0.5 on 2020-04-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20200410_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_date',
            name='name_slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
