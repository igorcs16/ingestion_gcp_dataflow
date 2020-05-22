# Ingestão de arquivos csv com DataFlow no GCP
Esse projeto tem o objetivo de fazer a ingestão de arquivos csv salvos no cloud storage no BigQuery usando DataFlow(Python),
conforme arquitetura;

![Alt text](img/Arquitetura.png?raw=true "Arquitetura")
Etapas:
1. Os arquivos price_quote.csv, bill_of_materials.csv e comp_boss.csv já estão salvos no bucket gs://data-dotz/

2. Para iniciar o processo de ingestão basta executar o script init_main.sh que será responsável por fazer o looping e acionar o main.py para criação dos jobs/pipelines no dataflow para cada arquivo.

2.1 Como executar e parâmetro: 
  $ bash init_main.sh project temp_location dataset
  $ sh init_main.sh project temp_location dataset
  $ ./init_main.sh project temp_location dataset
  - project: projeto no GCP
  - temp_location: local temporário para armazenar binários durante a execução das pipelines do dataflow
  - dataset: Dataset criado no BigQuery

![Alt text](img/Fluxograma.png?raw=true "Solução")
