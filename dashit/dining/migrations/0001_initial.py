# Generated by Django 3.0.2 on 2020-10-18 11:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('food_id', models.UUIDField(default=uuid.uuid4)),
                ('rating', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devices', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('wait', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DiningHall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('curr_wait', models.FloatField()),
                ('description', models.TextField()),
                ('foods', models.ManyToManyField(to='dining.Food')),
            ],
        ),
    ]
