# Generated by Django 2.2.5 on 2019-11-05 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlanguage',
            name='language',
            field=models.CharField(default='en', max_length=45, null=True),
        ),
    ]
