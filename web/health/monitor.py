# Garmin HR Monitor
# Uses ANT+ Protocol
# Abdallah Soliman

import sys
import time
from datetime import datetime
from asyncio import BaseEventLoop

from ant.core import driver, node
from ant.core.event import EventCallback
from ant.core.message import ChannelBroadcastDataMessage
from ant.core.constants import CHANNEL_TYPE_TWOWAY_RECEIVE, TIMEOUT_NEVER

class HRMon(EventCallback):

    # ANT Message Protocol Section 9.5.2.7
    NETWORK_KEYS = {
                "ant+": "\xB9\xA5\x21\xFB\xBD\x72\xC3\x45",
                "antfs": "\xA8\xA4\x23\xB9\xF5\x5E\x63\xC1",
                "public": "\xE8\xE4\x21\x3B\x55\x7A\x67\xC1"
            }


    def __init__(self, serial, network_key_type="ant+"):
        self.node = node.Node(driver.USB2Driver(serial))
        self.network_key_type = network_key_type
        self.channel = None

    def start(self):
        self.node.start()
        self._setup_channel(self.network_key_type)
        print "HRMon Started. Listening for Heart Rate..."


    def stop(self):
        if self.channel:
            self.channel.close()
            self.channel.unassign()
        if self.node:
            self.node.stop()


    def process(self, msg):
        if isinstance(msg, ChannelBroadcastDataMessage):
            print "%s - Heart Rate: %s" % (datetime.now().strftime("%I:%M:%S %m/%d/%y"), ord(msg.payload[-1]))


    def _network_key(self, type):
        key = self.NETWORK_KEYS.get(type)
        if key is None:
            raise Exception("Invalid network key type")
        else:
            return key


    def __enter__(self):
        return self


    def __exit__(self, type_, value, traceback):
        self.stop()


    def _setup_channel(self, network_key_type):
        key = node.NetworkKey(network_key_type, self._network_key(network_key_type))
        self.node.setNetworkKey(0, key)
        self.channel = self.node.getFreeChannel()
        self.channel.name = "HRM"
        self.channel.assign(network_key_type, CHANNEL_TYPE_TWOWAY_RECEIVE)
        self.channel.setID(120, 0, 0)
        self.channel.setSearchTimeout(TIMEOUT_NEVER)
        self.channel.setPeriod(8192)
        self.channel.setFrequency(57)
        self.channel.open()
        self.channel.registerCallback(self)


class MonitorEngine:

    def __init__(self):
        super(MonitorEngine, self).__init__(self)
        self.HRMon

    def run_forever(self):
        with HRMon('/dev/ttyUSB0', 'ant+') as hrm:
            hrm.start()
            while True:
                try:
                    time.sleep(2)
                except KeyboardInterrupt:
                    sys.exit(0)
