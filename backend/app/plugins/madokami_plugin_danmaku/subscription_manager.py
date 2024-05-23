from madokami.plugin.models import Subscription
from madokami.plugin.subscription import SubscriptionManager
from madokami.db import Session
from .crud import get_danmaku_storage, remove_danmaku_storage, add_danmaku_storage


class DanmakuSubscriptionManager(SubscriptionManager):
    def subscribe(self, session: Session, subscription: Subscription):
        add_danmaku_storage(session, subscription.data)

    def unsubscribe(self, session: Session, subscription_id: str):
        remove_danmaku_storage(session, subscription_id)

    def get_subscription(self, session: Session, subscription_id: str):
        pass

    def get_subscriptions(self, session: Session) -> list[Subscription]:
        return [Subscription(id=str(storage.id), name=storage.name, data=storage.link) for storage in get_danmaku_storage(session)]