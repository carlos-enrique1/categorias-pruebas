# Generated by Django 4.0 on 2022-03-07 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='tarea',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tareas.categoria'),
        ),
    ]
