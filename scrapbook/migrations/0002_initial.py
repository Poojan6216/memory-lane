# Generated by Django 5.1.3 on 2024-11-26 20:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scrapbook', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='memory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sharedaccess',
            name='memory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_with', to='scrapbook.memory'),
        ),
        migrations.AddField(
            model_name='sharedaccess',
            name='shared_with',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_memories', to=settings.AUTH_USER_MODEL),
        ),
    ]
