# survey/migrations/0003_add_initial_interests.py

from django.db import migrations

def create_interests(apps, schema_editor):
    Interest = apps.get_model('survey', 'Interest')
    interests = ['Sports', 'Music', 'Art', 'Technology', 'Travel', 'Reading']
    for interest_name in interests:
        Interest.objects.create(name=interest_name)

class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20241022_1547'),
    ]

    operations = [
        migrations.RunPython(create_interests),
    ]
