from consts import function


def get(player: "Player", item: str, feature: str):
    if (item, feature) in recipes:
        return recipes[(item, feature)](player)
    return None


def remove_input_feature(result: str, feature: str):
    """Returns a function that removes the feature and returns the result item"""
    
    def to_return(player: "Player"):
        area = player.wilderness[player.coordinates]
        area.remove_feature(feature)
        return result
    
    return to_return


def simple(result: str):
    """Returns a lambda function that returns the result in a simple manner"""
    return lambda x: result


recipes: dict[tuple[str, str]: function] = {
    ('axe', 'tree'): remove_input_feature('wood', 'tree'),
    ('knife', 'tall_grass'): remove_input_feature('grass', 'tall_grass'),
    ('raw_meat', 'campfire'): simple('cooked_meat')
}
