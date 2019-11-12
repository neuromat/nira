# Generated by Django 2.2.5 on 2019-11-12 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20190911_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectactivities',
            name='local',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to='person.Institution',
                verbose_name='Local'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='belongs_to',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to='activity.Meeting',
                verbose_name='Meeting'),
        ),
        migrations.AlterField(
            model_name='seminar',
            name='category',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to='activity.SeminarType',
                verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='trainingprogram',
            name='belongs_to',
            field=models.ForeignKey(blank=True,
                                    null=True,
                                    on_delete=django.db.models.deletion.PROTECT,
                                    to='activity.Meeting',
                                    verbose_name='Meeting'),
        ),
    ]
