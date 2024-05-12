from sqlmodel import Session

from madokami.plugin.models import Subscription
from madokami.plugin.subscription import SubscriptionManager
from .crud import get_rss_by_link, add_rss_storage, record_rss_history, get_rss_storages, remove_rss_storage


class MikanSubscriptionManager(SubscriptionManager):
    def subscribe(self, session: Session, subscription: Subscription):
        add_rss_storage(session, subscription.data, subscription.name)

    def unsubscribe(self, session: Session, subscription_id: str):
        remove_rss_storage(session, subscription_id)

    def get_subscription(self, session: Session, subscription_id: str):
        pass

    def get_subscriptions(self, session: Session) -> list[Subscription]:
        storages = get_rss_storages(session)
        return [Subscription(id=str(storage.id), name=storage.name, data=storage.rss_link) for storage in storages]