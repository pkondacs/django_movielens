import os
import shutil
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Deletes all migration files, __pycache__ directories, and the SQLite database'

    def handle(self, *args, **options):
        # Define the paths
        app_path = 'C:\\django_new\\django_movielens\\projectmovies\\movielens_app'
        commands_path = os.path.join(app_path, 'management', 'commands')
        database_path = 'C:\\django_new\\django_movielens\\projectmovies\\db.sqlite3'

        # Delete migration files
        migrations_path = os.path.join(app_path, 'migrations')
        if os.path.exists(migrations_path):
            for root, dirs, files in os.walk(migrations_path):
                for file in files:
                    if file.endswith('.py') and file != '__init__.py':
                        os.remove(os.path.join(root, file))
                    elif file.endswith('.pyc'):
                        os.remove(os.path.join(root, file))
            self.stdout.write(self.style.SUCCESS('Successfully deleted migration files.'))

        # Delete __pycache__ directory in commands
        pycache_path = os.path.join(commands_path, '__pycache__')
        if os.path.exists(pycache_path):
            shutil.rmtree(pycache_path)
            self.stdout.write(self.style.SUCCESS('Successfully deleted __pycache__ directory in commands.'))

        # Delete the database file
        if os.path.exists(database_path):
            os.remove(database_path)
            self.stdout.write(self.style.SUCCESS('Successfully deleted the SQLite database.'))
        else:
            self.stdout.write(self.style.WARNING('SQLite database file not found.'))
