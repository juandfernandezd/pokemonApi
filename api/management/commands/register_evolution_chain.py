from django.core.management.base import BaseCommand, CommandError
from api.functions import register_evolution


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('evolution_chain_id', type=int, help='Indicates the evolution chain id')

    def handle(self, *args, **options):
        evolution_chain_id = options['evolution_chain_id']
        message = register_evolution(evolution_chain_id)
        self.stdout.write(self.style.SUCCESS(message))
