from django.db import migrations

from api.user.models import User


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = User(name='boris',
                    email='borisboychev007@gmail.com',
                    is_staff=True,
                    is_superuser=True,
                    gender='Male')

        user.set_password('1234qwe')
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]