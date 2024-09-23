import asyncio

from app.core.configs.celery import celery
from app.infrastructure.neural.neural_infra import NeuralNetworkProcessor


@celery.task
def apply_neural_network():
    print("Starting apply_neural_network task...")
    asyncio.run(NeuralNetworkProcessor().run())
    print("Finished apply_neural_network task.")
