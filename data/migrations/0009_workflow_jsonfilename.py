# Generated by Django 2.0.3 on 2018-04-03 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_auto_20180401_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflow',
            name='jsonFileName',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]