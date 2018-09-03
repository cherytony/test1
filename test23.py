from abc import ABC, abstractmethod


class Talker(ABC):

    @abstractmethod
    def talk(self):
        pass


class Knigget(Talker):

    def talk(self):
        print("Ni!")


k = Knigget()
k.talk()
