
from pluginbase import PluginBase

plugin_source = PluginBase(package='plugins').make_plugin_source(searchpath=['./plugins'])
plugin_names = plugin_source.list_plugins()