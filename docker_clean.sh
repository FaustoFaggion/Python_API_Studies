#!/bin/bash

cd "~/Área de Trabalho/python_studies"

sudo docker compose down

sudo docker system prune -a

sudo docker volume rm python_studies_pg-data