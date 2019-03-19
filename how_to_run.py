from run_etl import main

result = main('Challenge_me.txt', 'pipelines/pipeline_one.json', 'price_prediction')
for line in result:
    print(line)
