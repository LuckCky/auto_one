from load import load_mapping
from utils.pipeline_actions import get_pipeline, get_actions_mapping


def main(data_file, pipeline_file, pipeline_name):
    pipeline = get_pipeline(pipeline_file, pipeline_name)
    actions = get_actions_mapping()
    for action_name, kwargs in pipeline:
        if action_name in load_mapping:
            action_index = pipeline.index([action_name, kwargs])
            pipeline[action_index][1]['source'] = data_file
            action = actions[action_name]
            result = action(**kwargs)
        else:
            action = actions[action_name]
            result = action(result, **kwargs)

    return result
