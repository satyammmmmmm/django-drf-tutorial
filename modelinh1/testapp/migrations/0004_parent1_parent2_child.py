# Generated by Django 4.1.1 on 2022-10-17 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_person_employee_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='parent1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(max_length=54)),
            ],
        ),
        migrations.CreateModel(
            name='parent2',
            fields=[
                ('f3', models.CharField(max_length=54, primary_key=True, serialize=False)),
                ('f4', models.CharField(max_length=54)),
            ],
        ),
        migrations.CreateModel(
            name='child',
            fields=[
                ('parent2_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='testapp.parent2')),
                ('parent1_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.parent1')),
                ('f5', models.CharField(max_length=54)),
                ('f6', models.CharField(max_length=54)),
            ],
            bases=('testapp.parent1', 'testapp.parent2'),
        ),
    ]
