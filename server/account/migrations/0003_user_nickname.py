# Generated by Django 3.2.6 on 2021-09-06 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_type_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, db_column='nickname', max_length=255, null=True),
        ),
    ]
