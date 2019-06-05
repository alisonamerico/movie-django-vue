# Generated by Django 2.2.2 on 2019-06-05 17:18

from django.db import migrations, models  # pragma: no cover


class Migration(migrations.Migration):  # pragma: no cover

    initial = True  # pragma: no cover

    dependencies = [  # pragma: no cover
    ]

    operations = [  # pragma: no cover
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=120)),
                ('genres', models.CharField(max_length=120)),
                ('duration', models.IntegerField()),
                ('title_year', models.IntegerField()),
                ('director_name', models.CharField(max_length=120)),
                ('imdb_score', models.DecimalField(decimal_places=1, max_digits=2)),
                ('picture', models.FileField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
        ),
    ]
