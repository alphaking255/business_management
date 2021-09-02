# Generated by Django 3.2.3 on 2021-08-21 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('amount', models.IntegerField(default=0)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('product_sold', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'ordering': ('-product_sold',),
            },
        ),
    ]
