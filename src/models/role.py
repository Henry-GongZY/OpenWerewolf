import abc

class Role(abc.ABC):
    def __init__(self, name: str, camp: str):
        """
        角色基类

        Args:
            name: 角色名称。
            camp: 角色阵营。
        """
        self.name = name
        self.camp = camp

    def __str__(self):
        return self.name
    
    @abc.abstractmethod
    def night_start(self, room):
        pass
