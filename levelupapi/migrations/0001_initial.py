# Generated by Django 3.1.3 on 2020-11-18 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('max_players', models.IntegerField()),
                ('game_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', related_query_name='game', to='levelupapi.gametype')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', related_query_name='game', to='levelupapi.gamer')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', related_query_name='event', to='levelupapi.gamer')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', related_query_name='event', to='levelupapi.game')),
                ('players', models.ManyToManyField(related_name='player_events', related_query_name='player_event', to='levelupapi.Gamer')),
            ],
        ),
    ]
