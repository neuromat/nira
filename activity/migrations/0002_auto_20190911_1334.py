# Generated by Django 2.2.5 on 2019-09-11 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('person', '0001_initial'),
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectactivities',
            name='local',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='person.Institution', verbose_name='Local'),
        ),
        migrations.AddField(
            model_name='news',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.ProjectActivities'),
        ),
        migrations.AddField(
            model_name='trainingprogram',
            name='belongs_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activity.Meeting', verbose_name='Meeting'),
        ),
        migrations.AddField(
            model_name='trainingprogram',
            name='speaker',
            field=models.ManyToManyField(to='person.Person', verbose_name='Speaker'),
        ),
        migrations.AddField(
            model_name='seminar',
            name='belongs_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='activity.Meeting', verbose_name='Meeting'),
        ),
        migrations.AddField(
            model_name='seminar',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.SeminarType', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='seminar',
            name='speaker',
            field=models.ManyToManyField(to='person.Person', verbose_name='Speaker'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='participant',
            field=models.ManyToManyField(blank=True, to='person.Person', verbose_name='Participant'),
        ),
    ]