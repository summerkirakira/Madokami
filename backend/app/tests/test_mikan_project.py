import pytest
from madokami import Launcher


def test_launcher():
    import app.plugins.mikan_project
    launcher = Launcher()
    engine = launcher.plugin_manager.get_engine_by_namespace("summerkirakira.mikan_project.mikan_downloader_engine")
    engine.run()
    a = 1
