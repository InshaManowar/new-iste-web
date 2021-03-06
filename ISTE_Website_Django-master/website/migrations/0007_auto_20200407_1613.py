# Generated by Django 3.0.2 on 2020-04-07 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20200407_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='date',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='category',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Event_Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=10)),
                ('start_date', models.DateTimeField()),
                ('end_end', models.DateTimeField(null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Event')),
            ],
        ),
    ]
