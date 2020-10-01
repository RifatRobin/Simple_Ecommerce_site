# Generated by Django 3.0.7 on 2020-09-27 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pName', models.CharField(max_length=30)),
                ('pDes', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('status', models.CharField(max_length=10)),
                ('mDate', models.DateField()),
                ('exDate', models.DateField()),
            ],
        ),
    ]
