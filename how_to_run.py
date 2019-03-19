import csv

from run_etl import main

result = main('Challenge_me.txt', 'pipelines/pipeline_one.json', 'price_prediction')
with open('result.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(result)
