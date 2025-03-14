from typing import Callable, Dict, List

class EventSystem:
    def __init__(self):
        # 事件监听器字典
        # key: 事件名称 (str)
        # value: 监听器列表 (List[Callable])
        self.listeners: Dict[str, List[Callable]] = {}

    def on(self, event_name: str, listener: Callable):
        """
        注册一个事件监听器。

        Args:
            event_name: 事件名称。
            listener: 事件监听器函数。
        """
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(listener)

    def off(self, event_name: str, listener: Callable):
        """
        移除一个事件监听器。

        Args:
            event_name: 事件名称。
            listener: 要移除的监听器函数。
        """
        if event_name in self.listeners:
            self.listeners[event_name].remove(listener)

    def emit(self, event_name: str, *args, **kwargs):
        """
        触发一个事件。

        Args:
            event_name: 事件名称。
            *args: 传递给监听器的位置参数。
            **kwargs: 传递给监听器的关键字参数。
        """
        if event_name in self.listeners:
            for listener in self.listeners[event_name]:
                listener(*args, **kwargs)

# 全局事件系统实例
event_system = EventSystem()
