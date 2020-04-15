# Generated by Django 3.0.5 on 2020-04-15 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('human', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Возраст')),
                ('gender', models.CharField(max_length=1, verbose_name='Пол')),
                ('human', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='human.Human', verbose_name='Human')),
            ],
        ),
    ]
