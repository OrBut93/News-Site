# Generated by Django 3.0.7 on 2020-06-22 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsSiteProj', '0005_auto_20200623_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('All', 'All'), ('Sport', 'Sport'), ('Education', 'Education'), ('Health', 'Health')], default='All', max_length=20),
        ),
    ]