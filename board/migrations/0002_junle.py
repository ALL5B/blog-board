# Generated by Django 2.0.2 on 2018-12-17 11:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Junle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ジャンル名')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
            ],
        ),
    ]