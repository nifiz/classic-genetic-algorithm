import json
from ..genetic_algorithm import GeneticAlgorithm

def results_to_json(ga_instance: GeneticAlgorithm, BestSolution: list, FitnessScore: float) -> str:
    field_dict = vars(ga_instance)

    # Make sure 'fields' is serializable - it can contain only primitives
    primitives = (bool, str, float, int, type(None))
    bad_keys = []
    for key in field_dict:
        if type(field_dict[key]) not in primitives:
            bad_keys.append(key)
    for bad_key in bad_keys:
        field_dict.pop(bad_key,None)

    # add the best solution and fitness score to the dict
    field_dict['Best Solution'] = ''.join(str(num) for num in BestSolution)
    field_dict['Fitness Score'] = FitnessScore

    return json.dumps(obj=field_dict, separators=(',\n',':'))
