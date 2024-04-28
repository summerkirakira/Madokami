import pytest
from madokami import get_app
from app.plugins.mikan_project.parser import MikanInfoPageParser
import requests
from app.plugins.mikan_project.bangumi_requester import BangumiRequester


@pytest.mark.skip(reason="This test is not working properly")
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
