# Generated by Django 3.2.6 on 2021-08-13 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0006_auto_20210813_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppinglist',
            name='items',
        ),
        migrations.AddField(
            model_name='shopitem',
            name='list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quickstart.shoppinglist'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shopitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.item'),
        ),
    ]
