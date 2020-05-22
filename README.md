# Ingestão de arquivos csv com DataFlow no GCP
O objetivo desse projeto é fazer a ingestão de arquivos csv salvos no cloud storage para o BigQuery usando DataFlow(Python),
conforme arquitetura;

![Alt text](img/Arquitetura.png?raw=true "Arquitetura")

## Pré-requisitos
- Versão do python: 3.7
- Instalar a dependência da lib apache-beam em requirements.txt - 'pip install -r requirements.txt'
- Criar um dataset no BigQuery para o armazenamento das tabelas

## Etapas:
1. Os arquivos price_quote.csv, bill_of_materials.csv e comp_boss.csv já estão salvos no bucket gs://data-dotz/

2. Para iniciar o processo de ingestão basta executar o script init_main.sh que será responsável por fazer o looping e acionar o main.py para criar os jobs/pipelines para cada arquivo no dataflow.

3. Como executar e parâmetros:

$ bash init_main.sh project temp_location dataset
  - project: projeto do GCP
  - temp_location: local temporário para armazenar binários durante a execução das pipelines do dataflow;
       exemplo: gs://dataflow-teste/temp
  - dataset: Dataset criado no BigQuery

![Alt text](img/Fluxograma.png?raw=true "Solução")
