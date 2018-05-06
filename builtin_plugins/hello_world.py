def hello_world():
    return {"code": -1}


def setup(app):
    print('-> Setting up : ' + __file__)
    app.register_function('hello_world', hello_world)