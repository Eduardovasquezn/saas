from typing import Any
from django.core.management.base import BaseCommand

# The class needs to be called Command
class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        print("hello world")