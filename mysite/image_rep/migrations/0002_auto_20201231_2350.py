# Generated by Django 3.1.4 on 2020-12-31 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image_rep', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_1',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_4',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_5',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/2020/12/31'),
        ),
        migrations.AddField(
            model_name='image',
            name='batch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='image_rep.batch'),
        ),
    ]
