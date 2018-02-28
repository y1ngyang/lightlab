'''Import all instrument module by name'''
import pkgutil
import lightlab
import pytest
import importlib

package = lightlab
modules = list()
for _, modname, _ in pkgutil.walk_packages(path=package.__path__,
                                           prefix=package.__name__ + '.',
                                           onerror=lambda x: None):
    modules.append(modname)


@pytest.mark.parametrize("modname", modules)
def test_import(modname):
    """Simply imports the module"""
    importlib.import_module(modname)
