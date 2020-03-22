# Generated by Django 2.1.3 on 2019-05-27 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0025_watershed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame', models.PositiveIntegerField()),
                ('comment', models.CharField(max_length=9999)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.Task')),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.AlterField(
            model_name='labels',
            name='category',
            field=models.CharField(default='category', max_length=256),
        ),
    ]