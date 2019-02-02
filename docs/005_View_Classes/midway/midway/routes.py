def includeme(config):
    config.add_route('addhorse', '/horse/add')
    config.add_route('delhorse', '/horse/delete')
    config.add_route('viewhorse', '/horse/{horseid}')
    config.add_route('racestanding', '/standings/race')
    config.add_route('horsestanding', '/standings/horses')
    config.add_route('viewhorse', '/race/{raceid}')
