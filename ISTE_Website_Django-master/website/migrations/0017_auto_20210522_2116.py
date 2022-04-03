# Generated by Django 3.0.5 on 2021-05-22 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_event_registration_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event_date',
            options={'ordering': ['start_date'], 'verbose_name': 'Dates of Events', 'verbose_name_plural': 'Dates of Events'},
        ),
        migrations.AddField(
            model_name='event_date',
            name='title',
            field=models.CharField(default='Default Title', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event_date',
            name='venue',
            field=models.CharField(max_length=100),
        ),
    ]
