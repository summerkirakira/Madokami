from madokami.internal.default_plugins.default_requester import DefaultRequester
from madokami import get_config
from typing import Optional, Any
import requests
from .models import BangumiSearchResult, BangumiSearchPostBody, EpisodeInfo, BangumiSubject


class BangumiRequester(DefaultRequester):
    def __init__(self):
        self.bangumi_token = get_config('madokami.config.bangumi_token', '8jkdHoKPLrOuI3WN8Xv5BLMp0MgAZ5Dk7KXP2i4j')
        headers = {
            'user-agent': 'summerkirakira/Madokami (https://github.com/summerkirakira/Madokami)',
            'Authorization': f'Bearer {self.bangumi_token}'
        }
        self.api_url = 'https://api.bgm.tv'
        super().__init__(headers=headers)

    def cancel(self):
        pass

    def search(self, query: str) -> BangumiSearchResult:
        url = f'{self.api_url}/v0/search/subjects'
        post_body = BangumiSearchPostBody(keyword=query)
        response = self.request(url, method='POST', data=post_body.model_dump(mode='json'))
        return BangumiSearchResult.model_validate(response.json())

    def get_episode_info(self, bangumi_id: int, type=0, limit=100, offset=0) -> EpisodeInfo:
        url = f'{self.api_url}/v0/episodes?subject_id={bangumi_id}&type={type}&limit={limit}&offset={offset}'
        response = self.request(url, method='GET')
        return EpisodeInfo.model_validate(response.json())

    def get_subject(self, bangumi_id: int) -> BangumiSubject:
        url = f'{self.api_url}/v0/subjects/{bangumi_id}'
        response = self.request(url, method='GET')
        return BangumiSubject.model_validate(response.json())

    def get_subject_image(self, bangumi_id: int, type='large') -> bytes:
        url = f'{self.api_url}/v0/subjects/{bangumi_id}/image?type={type}'
        response = self.request(url, method='GET')
        return response.content

    @property
    def namespace(self) -> str:
        return 'summerkirakira.mikan_project.bangumi_requester'

    @property
    def name(self) -> str:
        return 'Bangumi Requester'


@property
def description(self) -> str:
    pass