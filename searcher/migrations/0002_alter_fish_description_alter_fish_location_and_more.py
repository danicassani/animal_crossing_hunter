# Generated by Django 4.2.4 on 2023-09-02 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='description',
            field=models.TextField(default='No description available.'),
        ),
        migrations.AlterField(
            model_name='fish',
            name='location',
            field=models.CharField(choices=[('River', 'River'), ('Pond', 'Pond'), ('Sea', 'Sea'), ('River Mouth', 'River Mouth'), ('Waterfall', 'Waterfall'), ('Pier', 'Pier')], max_length=200),
        ),
        migrations.AlterField(
            model_name='fish',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fish',
            name='season_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fish',
            name='season_start',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='insect',
            name='description',
            field=models.TextField(default='No description available.'),
        ),
        migrations.AlterField(
            model_name='insect',
            name='location',
            field=models.CharField(choices=[('Tree', 'Tree'), ('Flower', 'Flower'), ('Ground', 'Ground'), ('Rock', 'Rock'), ('Stump', 'Stump'), ('Trash', 'Trash'), ('Flying', 'Flying')], max_length=200),
        ),
        migrations.AlterField(
            model_name='insect',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='insect',
            name='season_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='insect',
            name='season_start',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seacreature',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seacreature',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='seacreature',
            name='season_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seacreature',
            name='season_start',
            field=models.DateField(blank=True, null=True),
        ),
    ]