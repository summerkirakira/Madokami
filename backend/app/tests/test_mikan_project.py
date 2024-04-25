import pytest
from madokami import get_app
from app.plugins.mikan_project.parser import MikanInfoPageParser
from madokami.internal.default_plugins.default_requester import DefaultRequester
import requests



def test_launcher():
    app = get_app()
    engine = app.plugin_manager.get_engine_by_namespace("summerkirakira.mikan_project.mikan_downloader_engine")
    engine.run()
    while True:
        pass


@pytest.mark.skip(reason="This test is not working properly")
def test_mikan_info_parser():
    mikan_info_parser = MikanInfoPageParser()
    info_page = requests.get("https://mikanani.me/Home/Bangumi/3239")
    mikan_info_parser.parse(info_page.text)
