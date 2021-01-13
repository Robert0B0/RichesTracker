# Generated by Django 3.1.1 on 2020-11-30 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monetaryrecord',
            name='category',
            field=models.CharField(choices=[('Outcome', (('expenses', 'Expenses'), ('upkeep', 'Upkeep'), ('unforeseen', 'Unforeseen'), ('Goal Complete', 'Goal Complete'), ('Investment', 'Investment'), ('Saving tipped', 'Saving tipped'))), ('Income', (('monthly income', 'Monthly Income'), ('dividents', 'Dividents'), ('saving jar', 'Saving Jar'), ('other', 'Other')))], default='Outcome', max_length=200),
        ),
    ]
