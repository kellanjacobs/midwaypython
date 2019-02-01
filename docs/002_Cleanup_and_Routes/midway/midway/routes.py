def includeme(config):
    config.add_route('addhorse', '/horse/add')
    config.add_route('delhorse', '/horse/delete')
    config.add_route('viewhorse', '/horse/{horseid}')
