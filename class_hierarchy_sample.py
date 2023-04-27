# task to create interfaces
from abc import ABC, abstractmethod


class CallDevice(ABC):
    @abstractmethod
    def call():
        pass


class SmsDevice(ABC):
    @abstractmethod
    def sms():
        pass


class SearvDevice(ABC):
    @abstractmethod
    def search():
        pass


class MobilePhone(CallDevice, SmsDevice, SearvDevice):

    def call():
        pass

    def sms():
        pass

    def search():
        pass


class BabushkaPhone(CallDevice):

    def call():
        pass
