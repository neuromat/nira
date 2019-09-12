# Generated by Django 2.2.5 on 2019-09-11 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dissemination', '0001_initial'),
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='internal',
            name='author',
            field=models.ManyToManyField(blank=True, to='person.Person', verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='internal',
            name='media_outlet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dissemination.InternalMediaOutlet', verbose_name='Media outlet'),
        ),
        migrations.AddField(
            model_name='external',
            name='author',
            field=models.ManyToManyField(blank=True, to='person.Person', verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='external',
            name='media_outlet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dissemination.ExternalMediaOutlet', verbose_name='Media outlet'),
        ),
    ]