# Generated by Django 3.0.5 on 2022-03-25 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_auto_20220325_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='github',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='instagram',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='linkedin',
            field=models.CharField(default=None, max_length=150, null=True),
        ),
    ]
