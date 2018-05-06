# -*- coding: utf-8 -*-
import os
from functools import partial
from pluginbase import PluginBase
import schedule
import time
import upload_github

# relative path
here = os.path.abspath(os.path.dirname(__file__))
get_path = partial(os.path.join, here)
# Setup a plugin base, and load builtin plugins
plugin_base = PluginBase(package=os.path.basename(__file__).split('.')[0]+'.plugins',
                         searchpath=[get_path('./builtin_plugins')])


class Application(object):
    """load plugins Class"""
    def __init__(self, name):
        self.name = name

        # functions provided by plugins
        self.functions = {}

        # load plugins of "{app_name}/plugins"
        self.source = plugin_base.make_plugin_source(
            searchpath=[get_path('./%s/plugins' % name)],
            identifier=self.name)

        # initialize plugins by setup
        for plugin_name in self.source.list_plugins():
            plugin = self.source.load_plugin(plugin_name)
            plugin.setup(self)

    def register_function(self, name, plugin_function):
        self.functions[name] = plugin_function


def run(app):
    """run plugins"""
    # print("run plugins of {name}".format(name=app.name))
    for name, func in sorted(app.functions.items()):
        try:
            result = func()
            if result['code'] == -1:
                continue
            else:
                print('{name} : {result}'.format(name=name, result=result))
                upload_github.upload(result)
        except Exception as error:
            print(error)

def main():
    # Set up applications
    app = Application('app')
    run(app)

    schedule.every(24).to(26).hours.do(run, app)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()

