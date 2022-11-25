#!/usr/bin/env python

import sys
from swarm.msg import Detection
import Classes.receiver


while(True):
    Classes.receiver.background_controller(Detection.relative_bearing, Detection.right_detection)