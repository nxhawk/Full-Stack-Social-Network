# Generated by Django 4.2.5 on 2023-10-08 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_comments_count_comment_post_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.CharField(max_length=255)),
                ('occurences', models.IntegerField()),
            ],
        ),
    ]