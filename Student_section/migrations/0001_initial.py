# Generated by Django 4.0.5 on 2022-06-23 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_table',
            fields=[
                ('Member_IdNumber', models.IntegerField(primary_key=True, serialize=False)),
                ('Member_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Profession', models.CharField(blank=True, max_length=20, null=True)),
                ('Email', models.EmailField(blank=True, max_length=40, null=True)),
                ('Phone_No', models.CharField(blank=True, max_length=10, null=True)),
                ('Set_Username', models.CharField(blank=True, max_length=40, null=True)),
                ('Set_Password', models.CharField(blank=True, max_length=40, null=True)),
                ('membership_plan', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
    ]