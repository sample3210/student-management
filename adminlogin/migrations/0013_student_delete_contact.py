# Generated by Django 4.2 on 2023-04-18 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlogin', '0012_alter_contact_remarks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('fathername', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('contact_no', models.CharField(max_length=20)),
                ('class_name', models.CharField(max_length=20)),
                ('remarks', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
