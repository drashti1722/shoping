# Generated by Django 3.2.7 on 2021-11-25 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='shpping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('price', models.PositiveBigIntegerField()),
                ('colour', models.CharField(max_length=10)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopp.category')),
            ],
        ),
    ]
