import logging
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

# Configure logger
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Creates a default admin user if one doesn't exist."

    def handle(self, *args, **kwargs):
        User = get_user_model()

        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "adminpassword")
            message = "Admin user created."
            logger.info(message)
        else:
            message = "Admin user already exists."
            logger.warning(message)
