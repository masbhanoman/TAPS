# Generated by Django 2.2.6 on 2019-10-26 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_type',
            name='title',
            field=models.CharField(default='test1', max_length=200),
            preserve_default=False,
        ),
    ]