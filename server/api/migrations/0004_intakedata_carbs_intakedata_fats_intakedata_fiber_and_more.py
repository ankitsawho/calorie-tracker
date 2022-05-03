# Generated by Django 4.0.4 on 2022-04-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='intakedata',
            name='carbs',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='intakedata',
            name='fats',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='intakedata',
            name='fiber',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='intakedata',
            name='proteins',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True),
        ),
    ]
