# Generated by Django 3.0.3 on 2020-04-29 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to=None)),
                ('property_description', models.TextField()),
                ('price_per_day', models.IntegerField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Address')),
                ('posted_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('total_price', models.IntegerField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.Property')),
                ('renter', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=None)),
                ('Property', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='rentals.Property')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('comment', models.TextField()),
                ('reservation', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='rentals.Reservation')),
            ],
        ),
    ]
