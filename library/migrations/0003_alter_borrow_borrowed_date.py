# Generated by Django 5.1.2 on 2024-11-27 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_borrow_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='borrowed_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]