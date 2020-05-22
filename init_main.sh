#!/bin/bash 

if [ $# -ne 3 ]; then
  echo "run ./init_main.sh project temp_location dataset"
  exit 1
fi

runner="DataflowRunner"
job_names="price-quote\ncomp-boss\nbill-of-materials"
project=$1
temp_location=$2
dataset=$3

for i in `echo -e $job_names`
do
  table=`echo $i | tr "-" "_"`
  python main.py --project $project --runner $runner --temp_location $temp_location --output $dataset"."$table --job_name $i
done
