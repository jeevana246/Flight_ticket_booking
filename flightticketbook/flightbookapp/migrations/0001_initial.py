# Generated by Django 3.2.3 on 2022-11-16 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='flight_details',
            fields=[
                ('flight_code', models.TextField(max_length=20, primary_key=True, serialize=False)),
                ('airline', models.TextField(max_length=100)),
                ('source', models.TextField(max_length=100)),
                ('destination', models.TextField(max_length=100)),
                ('dep_date', models.DateTimeField()),
                ('arrival_date', models.DateTimeField()),
                ('price', models.FloatField()),
                ('tot_seat_count', models.IntegerField(default=60)),
                ('vacc_count', models.IntegerField(default=60)),
            ],
        ),
        migrations.CreateModel(
            name='personal_det',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=200)),
                ('phonenum', models.TextField(max_length=20)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking_det',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=200)),
                ('flight_code', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='flightbookapp.flight_details')),
            ],
        ),
    ]