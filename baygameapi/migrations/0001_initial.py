# Generated by Django 4.1.7 on 2023-03-15 20:35

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
            name='BayItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('default_img', models.CharField(max_length=250)),
                ('found_img', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Gamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Occasion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('emoji', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='RiverAndStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('miles_to_bay', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='RecordOfTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=55)),
                ('number_found', models.IntegerField()),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gamer_id', to='baygameapi.gamer')),
                ('occasion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='baygameapi.occasion')),
            ],
        ),
        migrations.CreateModel(
            name='FoundItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bay_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item_found', to='baygameapi.bayitem')),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gamer_found', to='baygameapi.gamer')),
            ],
        ),
        migrations.AddField(
            model_name='bayitem',
            name='gamers',
            field=models.ManyToManyField(related_name='gamers_who_found_item', through='baygameapi.FoundItem', to='baygameapi.gamer'),
        ),
    ]
