# Generated by Django 3.0.7 on 2020-06-22 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsSiteProj', '0004_auto_20200623_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('S', 'Sport'), ('E', 'Education'), ('H', 'Health')], default='S', max_length=20),
        ),
    ]
