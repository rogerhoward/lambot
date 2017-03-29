#!/usr/bin/env python
import os, sys
from pluginbase import PluginBase

plugin_base = PluginBase(package='plugins')
plugin_source = plugin_base.make_plugin_source(searchpath=['./plugins'])
plugin_names = plugin_source.list_plugins()

print(plugin_names)

for plugin_name in plugin_names:
    plugin = plugin_source.load_plugin(plugin_name)
    plugin_instance = plugin.Action({'cool': 'beans', 'text':'hello world!'})
    print(plugin_instance.response)