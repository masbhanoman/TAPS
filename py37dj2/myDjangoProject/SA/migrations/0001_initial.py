# Generated by Django 2.2.12 on 2020-04-13 09:35

import SA.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(default='New Buyer', max_length=50)),
                ('buyer_brand', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ('buyer_name',),
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, default='New Customer', max_length=30, null=True, unique=True)),
            ],
            options={
                'ordering': ('customer_name',),
            },
        ),
        migrations.CreateModel(
            name='CustomerGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_group_name', models.CharField(default='New Customer Group', max_length=30)),
                ('customer_name', models.ManyToManyField(to='SA.Customer')),
            ],
            options={
                'ordering': ('customer_group_name',),
            },
        ),
        migrations.CreateModel(
            name='Finish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finish_name', models.CharField(default='finish', max_length=30)),
                ('finish_category', models.CharField(choices=[('15', 'Silver'), ('12', 'Gunmetal'), ('10', 'Copper'), ('07', 'Tin'), ('03', 'Zinc'), ('07', 'Dyeing'), ('03', 'Paint')], default='None', help_text='bath name', max_length=30)),
                ('Default_finish_code', models.CharField(blank=True, help_text='tex finish book', max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SA_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(blank=True, default=SA.models.new_sa_number, max_length=10, null=True)),
            ],
            options={
                'ordering': ('item_id',),
            },
        ),
        migrations.CreateModel(
            name='Salesman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salesman_id', models.CharField(max_length=7)),
                ('salesman_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='SA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sa_number', models.CharField(blank=True, default=SA.models.new_sa_number, max_length=500, null=True)),
                ('booking_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('production_del_date', models.DateField(blank=True, null=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('15', 'Normal'), ('12', 'Urgent'), ('10', 'Speed'), ('07', 'Fire Urgent'), ('03', 'Super Fire Urgent')], default=15, max_length=2)),
                ('style', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=10)),
                ('washing_type', models.CharField(max_length=10)),
                ('wash_ref', models.CharField(max_length=50)),
                ('other_requirements', models.TextField(max_length=50)),
                ('b_c_d_part_finish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SA.Finish')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SA.Buyer')),
                ('sa_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sa_customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SA.CustomerGroup')),
                ('sa_item', models.ManyToManyField(to='SA.SA_Item')),
                ('salesman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SA.Salesman')),
            ],
            options={
                'ordering': ('sa_number',),
            },
        ),
    ]
