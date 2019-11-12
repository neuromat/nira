# Generated by Django 2.2.5 on 2019-11-12 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scientific_mission', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='destination_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='destination', to='cities_light.City', verbose_name='To'),
        ),
        migrations.AlterField(
            model_name='route',
            name='origin_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='origin', to='cities_light.City', verbose_name='From'),
        ),
        migrations.AlterField(
            model_name='scientificmission',
            name='destination_city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='destination_city', to='cities_light.City', verbose_name='City of destination'),
        ),
        migrations.AlterField(
            model_name='scientificmission',
            name='mission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='scientific_mission.Type', verbose_name='Mission'),
        ),
        migrations.AlterField(
            model_name='scientificmission',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='person.Person', verbose_name='Paid to'),
        ),
        migrations.AlterField(
            model_name='scientificmission',
            name='project_activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='activity.ProjectActivities', verbose_name='Project activity'),
        ),
    ]
