# Generated by Django 5.1.4 on 2024-12-15 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_productcategory_delete_question_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='hiha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sla', models.TextField()),
            ],
        ),
    ]