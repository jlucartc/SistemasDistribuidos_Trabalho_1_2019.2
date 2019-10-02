# -*- coding:utf-8 -*-

import _thread
from ReceiveUDP import ReceiveUDP

rcvs = []
rcvs_q = 3;

for i in range(0,rcvs_q):

    rcvs.append(ReceiveUDP("224.1.1.1",9998))

for i in range(0,len(rcvs)):

    rcvs[i].start()
