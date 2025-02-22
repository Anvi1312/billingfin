# Generated by Django 5.1.5 on 2025-01-29 18:24

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='stock',
        ),
        migrations.AddField(
            model_name='medicine',
            name='description',
            field=models.TextField(default='No description provided'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='expiry_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='medicine',
            name='manufacturer',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='medicine',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='medicine',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='inventory.category'),
        ),
    ]
