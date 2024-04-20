from stevedore import extension
from ..plugins import get_plugins
from typing import Optional, Type
from ..core.interface.requester import RequesterInterface


class Extension:
    def __init__(self, name, plugin):
        self.name = name
        self.plugin = plugin


def get_extensions() -> list[Extension]:
    external_extensions = extension.ExtensionManager(
        namespace='',
        invoke_on_load=False
    )

    internal_extensions = [Extension(ext.namespace, ext) for ext in get_plugins()]
    external_extensions = [Extension(ext.name, ext.plugin) for ext in external_extensions]

    return internal_extensions + external_extensions


def get_extension(name: str) -> Optional[Extension]:
    for ext in get_extensions():
        if ext.name == name:
            return ext
    return None


def get_plugin_by_type(plugin_type: str) -> list[Extension]:
    return [ext for ext in get_extensions() if ext.name.startswith(plugin_type)]


def get_requester(name: str) -> Optional[Type[RequesterInterface]]:
    ext = get_extension(name)
    if ext is not None:
        return ext.plugin
    return None
