from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Clear database and reseed with fresh test data"

    def handle(self, *args, **kwargs):
        self.stdout.write(" Clearing DB and reseeding...")

        # Flush DB (clear data but keep migrations)
        call_command("flush", "--noinput")

        # Run migrations
        call_command("migrate")

        # Seed with fresh data
        call_command("seed")

        self.stdout.write(self.style.SUCCESS("Database flushed, migrated, and reseeded"))
