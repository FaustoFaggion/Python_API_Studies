#!/bin/bash

cd "~/Área de Trabalho/python_studies"

sudo docker compose down

sudo docker system prune -a

sudo docker volume rm postgres_pg-data