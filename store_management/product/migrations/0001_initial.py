# Generated by Django 3.2.3 on 2021-09-04 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productcategory')),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
    ]
