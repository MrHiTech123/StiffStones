from consts import function
from typing import NamedTuple


class UsageRecipe(NamedTuple):
    result: str
    result_function: function


def get(player: "Player", item: str, feature: str):
    result = get_recipe(item, feature)
    if result == None:
        return None
    return result.result_function(player)

def get_recipe(item: str, feature: str):
    """Get the result item, if there is one, from using an item on a feature"""
    if (item, feature) in registry:
        return registry[(item, feature)]
    return None


def remove_input_feature(result: str, feature: str):
    """Returns a function that removes the feature and returns the result item"""
    
    def to_be_result_function(player: "Player"):
        area = player.get_current_area()
        area.remove_feature(feature)
        return result
    
    return UsageRecipe(result, to_be_result_function)


def simple_function(result: str):
    """Returns a lambda function that returns the result in a simple manner"""
    return lambda x: result


def simple(result: str):
    return UsageRecipe(result, simple_function(result))


# Recipe registry
registry: dict[tuple[str, str]: function] = {
    ('axe', 'tree'): remove_input_feature('wood', 'tree'),
    ('knife', 'tall_grass'): remove_input_feature('grass', 'tall_grass'),
    ('raw_meat', 'campfire'): simple('cooked_meat'),
    ('spear', 'rabbit'): remove_input_feature('raw_meat', 'rabbit'),
}
