#!/bin/sh

echo "Waiting for RabbitMQ..."

while ! nc -z rabbitmq3 5672; do
  sleep 0.1
done

echo "RabbitMQ started!"

exec "$@"