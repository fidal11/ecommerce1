# Generated by Django 4.2.1 on 2023-05-15 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customername', models.CharField(max_length=100)),
                ('customermobile', models.BigIntegerField()),
                ('customermail', models.CharField(max_length=100)),
                ('customerpassword', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Seller1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sellername', models.CharField(max_length=100)),
                ('mobileno', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
                ('companyname', models.CharField(max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
                ('username', models.IntegerField(default=1)),
                ('ac_holder_name', models.CharField(default='', max_length=30)),
                ('ifsc', models.CharField(default='', max_length=20)),
                ('branch', models.CharField(default='', max_length=30)),
                ('ac_no', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(upload_to='seller/')),
                ('gender', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
