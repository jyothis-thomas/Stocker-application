# Generated by Django 2.2.5 on 2019-10-09 08:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quotes', '0004_auto_20191009_0611'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stock',
            unique_together={('ticker', 'user')},
        ),
    ]
