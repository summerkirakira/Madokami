import pytest
from madokami import get_app
from app.plugins.mikan_project.parser import MikanSearchItemParser, MikanInfoPageParser
import requests
from madokami.internal.default_plugins.bangumi_requester import BangumiRequester


@pytest.mark.skip(reason="This test is not working properly")
def test_mikan_downloader_engine():
    app = get_app()
    engine = app.plugin_manager.get_engine_by_namespace("summerkirakira.mikan_project.mikan_downloader_engine")
    engine.run()
    while True:
        pass


def test_whole_app():
    app = get_app()
    app.start()
    while True:
        ...


@pytest.mark.skip(reason="This test is not working properly")
def test_mikan_info_parser():
    mikan_search_parser = MikanSearchItemParser()
    mikan_info_page_parser = MikanInfoPageParser()
    info_page = requests.get("https://mikanani.me/Home/Bangumi/3239")
    result = mikan_search_parser.parse(info_page.text)
    assert result is not None
    result = mikan_info_page_parser.parse(info_page.text)
    assert result is not None


@pytest.mark.skip(reason="This test is not working properly")
def test_bangumi_requester():
    requester = BangumiRequester()
    result = requester.search("魔法少女小圆")
    assert result is not None
    result = requester.get_episode_info(9717)
    assert result is not None
    result = requester.get_subject(9717)
    assert result is not None
    result = requester.get_subject_image(9717)
    assert result is not None
