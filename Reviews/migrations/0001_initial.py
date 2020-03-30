# Generated by Django 3.0.4 on 2020-03-27 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('Course_Code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('Department', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=250)),
                ('Rating', models.DecimalField(decimal_places=3, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Professors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=50)),
                ('Rating', models.DecimalField(decimal_places=3, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Professor_Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Upvotes', models.IntegerField()),
                ('Anonymous', models.BooleanField()),
                ('Date', models.DateField()),
                ('Professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reviews.Professors')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course_Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Upvotes', models.IntegerField()),
                ('Anonymous', models.BooleanField()),
                ('Date', models.DateField()),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reviews.Courses')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]