import argparse
import logging
import re
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import os
from schemas import price_quote, comp_boss, bill_of_materials

class DataParse:
    def __init__(self, schema):
        self.fields = tuple( i for i in schema.keys())

    # Converte em um dicionario para que possa ser salvo no BQ
    def parse_method(self, string_input):
        values = re.split(",",re.sub('\r\n', '', re.sub(u'"', '', string_input)))
        row = dict(zip(self.fields,values))
        return row

def run(argv=None):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--input',
        dest='input',
        required=False,
        help='Input file to read. This can be a local file or '
        'a file in a Google Storage Bucket.',
        default='gs://data-dotz/')

    parser.add_argument(
        '--output',
        dest='output',
        required=True,
        help='Output BQ table to write results to.')

    #Argumentos passados por linha de comando
    known_args, pipeline_args = parser.parse_known_args(argv)

    if pipeline_args[-1] == 'price-quote':
        known_args.input = known_args.input + "price_quote.csv"
        schema = price_quote()
    elif pipeline_args[-1] == 'comp-boss':
        known_args.input = known_args.input + "comp_boss.csv"
        schema = comp_boss()
    else:
        known_args.input = known_args.input + "bill_of_materials.csv"
        schema = bill_of_materials()

    data = DataParse(schema)
    bq_schema = ",".join(["{}:{}".format(k,v) for k,v in schema.items()])

    #Salva as opcoes passadas como parâmetro para a pipeline
    p = beam.Pipeline(options=PipelineOptions(pipeline_args))

    (
    # Lê os dados do arquivo csv
     p | 'Read storage' >> beam.io.ReadFromText(known_args.input,skip_header_lines=1)
    # Converte para as linhas do BQ
     | 'BigQuery Row' >> beam.Map(lambda s: data.parse_method(s))
    # Escreve no BQ
     | 'Write to BigQuery' >> beam.io.Write(
         beam.io.BigQuerySink(
             known_args.output,
             schema=bq_schema,
             create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
             write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE)))
    p.run().wait_until_finish()


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()