# Generated by Django 3.2.4 on 2021-06-04 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210605_0139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='data_created',
            new_name='date_created',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
