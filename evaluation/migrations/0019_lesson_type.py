# Generated by Django 2.2.7 on 2019-11-29 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0018_auto_20191129_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='type',
            field=models.CharField(choices=[('A', 'Assesment'), ('L', 'Lesson')], default='L', max_length=1),
        ),
    ]
