# Generated by Django 2.1.3 on 2018-11-20 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0003_auto_20181120_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='category',
            field=models.ManyToManyField(db_index=True, related_name='lectures', to='lecture.Category', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='classroom',
            field=models.CharField(blank=True, db_index=True, max_length=16, null=True, verbose_name='classroom'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='code',
            field=models.CharField(db_index=True, max_length=16, verbose_name='lecture id'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='point',
            field=models.FloatField(blank=True, db_index=True, default=1.0, null=True, verbose_name='point'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='professor',
            field=models.CharField(blank=True, db_index=True, max_length=32, null=True, verbose_name='professor'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='subcategory',
            field=models.ManyToManyField(db_index=True, related_name='lectures', to='lecture.Subcategory', verbose_name='subcategory'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='title',
            field=models.CharField(db_index=True, max_length=64, verbose_name='title'),
        ),
    ]
