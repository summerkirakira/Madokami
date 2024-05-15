from sqlmodel import Session

from madokami.plugin.models import Subscription
from madokami.plugin.subscription import SubscriptionManager
from .crud import get_rss_by_link, add_rss_storage, record_rss_history, get_rss_storages, remove_rss_storage
from .models import MikanRssStorage
from typing import Optional, Tuple


def convert_storage_to_str(storage: MikanRssStorage) -> str:
    if storage.preferred_pattern is None:
        storage.preferred_pattern = ''
    if storage.banned_pattern is None:
        storage.banned_pattern = ''
    return f'{storage.rss_link}#{storage.preferred_pattern.replace("#", ",")}|{storage.banned_pattern.replace("#", ",")}'


def convert_str_to_storage(data: str) -> Tuple[str, Optional[str], Optional[str]]:
    if '#' in data:
        rss_link, patterns = data.split('#')
        if '|' not in patterns:
            return rss_link, patterns.replace(',', "#"), None
        preferred_pattern, banned_pattern = patterns.split('|')
        return rss_link, preferred_pattern.replace(',', '#'), banned_pattern.replace(',', '#')
    else:
        if '|' in data:
            rss_link, patterns = data.split('|')
            return rss_link, None, patterns.replace(',', '#')
        else:
            return data, None, None


class MikanSubscriptionManager(SubscriptionManager):
    def subscribe(self, session: Session, subscription: Subscription):
        rss_link, preferred_pattern, banned_pattern = convert_str_to_storage(subscription.data)
        add_rss_storage(session, rss_link, subscription.name, preferred_pattern=preferred_pattern, banned_pattern=banned_pattern)

    def unsubscribe(self, session: Session, subscription_id: str):
        remove_rss_storage(session, subscription_id)

    def get_subscription(self, session: Session, subscription_id: str):
        pass

    def get_subscriptions(self, session: Session) -> list[Subscription]:
        storages = get_rss_storages(session)
        return [Subscription(id=str(storage.id), name=storage.name, data=convert_storage_to_str(storage).replace("#|", "")) for storage in storages]