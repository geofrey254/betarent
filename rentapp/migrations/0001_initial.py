# Generated by Django 4.0.2 on 2022-02-11 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True, unique=True)),
                ('slug', models.SlugField(max_length=250, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('list_img', models.ImageField(blank=True, null=True, upload_to='house_pics/')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('agent', models.CharField(default='Beta Rent', max_length=100)),
                ('agent_img', models.ImageField(blank=True, null=True, upload_to='agent_pics/')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('body', models.CharField(max_length=5000, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('house_type', models.IntegerField(choices=[(0, 'None'), (1, 'Featured')], default=0)),
                ('categories', models.ManyToManyField(related_name='lists', to='rentapp.Category')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
