# Generated by Django 4.2.5 on 2023-10-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_friends_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends_count',
            field=models.IntegerField(default=0),
        ),
    ]
