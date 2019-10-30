# Generated by Django 2.2.6 on 2019-10-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_type_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('title',)},
        ),
        migrations.AlterModelOptions(
            name='post_type',
            options={'ordering': ('title',)},
        ),
        migrations.AddField(
            model_name='post_type',
            name='category',
            field=models.ManyToManyField(to='blog.Post'),
        ),
    ]