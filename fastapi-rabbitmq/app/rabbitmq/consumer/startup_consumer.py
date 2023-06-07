import asyncio
import aio_pika
import os

username = os.environ.get("RABBITMQ_USER")
password = os.environ.get("RABBITMQ_PASSWORD")
host = os.environ.get("RABBITMQ_HOST")
port = os.environ.get("RABBITMQ_PORT")

async def rabbitmq_consumer(loop):
    connection = await aio_pika.connect_robust(
        f"amqp://{username}:{password}@{host}:{port}/", loop=loop
    )

    async with connection:
        channel = await connection.channel()

        exchange = await channel.declare_exchange('my_exchange', aio_pika.ExchangeType.TOPIC)

        queue_1 = await channel.declare_queue('queue_1')
        queue_2 = await channel.declare_queue('queue_2')

        # Bind queues to topics
        await queue_1.bind(exchange, 'topic_1')
        await queue_2.bind(exchange, 'topic_2')

        async def process_message(message: aio_pika.IncomingMessage):
            async with message.process():
                print("Received message: %s" % message.body)

        # Set up consumers for each queue
        await queue_1.consume(process_message)
        await queue_2.consume(process_message)

        while True:
            # Continue consuming messages
            await asyncio.sleep(1)