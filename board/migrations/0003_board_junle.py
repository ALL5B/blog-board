# Generated by Django 2.0.2 on 2018-12-17 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_junle'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='junle',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='board.Junle', verbose_name='ジャンル'),
        ),
    ]