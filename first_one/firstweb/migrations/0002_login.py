# Generated by Django 2.0.5 on 2019-04-30 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
