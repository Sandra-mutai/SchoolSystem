# Generated by Django 3.2.5 on 2021-09-16 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0004_auto_20210916_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='bank_account',
            field=models.IntegerField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='company',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='contract',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='country',
            field=models.CharField(choices=[('Kenya', 'Kenya'), ('Uganda', 'Uganda'), ('Rwanda', 'Rwanda')], default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trainer',
            name='resume',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trainer',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='nationality',
            field=models.CharField(choices=[('Kenyan', 'Kenyan'), ('Rwandese', 'Rwandese'), ('Ugandan', 'Ugandan'), ('Sudanese', 'Sudanese'), ('South Sudanese', 'South Sudanese'), ('Somalia', 'Somalia')], max_length=15, null=True),
        ),
    ]
