#!/usr/bin/python
import os
import re
import signal
import select
from subprocess import Popen, PIPE, STDOUT
from mininet.util import ( quietRun, errRun, errFail, moveIntf, isShellBuiltin,
                           numCores, retry, mountCgroups )
from mininet.net import Mininet
from mininet.node import OVSForest
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def ovsns():

  net = Mininet( topo=None, build=False, switch=OVSForest )
  h1 = net.addHost('h1')
  h2 = net.addHost('h2')
  s1 = net.addSwitch('s1')
  s2 = net.addSwitch('s2')
#  c0 = net.addController('c20')

  net.addLink(h1, s1)
  net.addLink(s1, s2)
  net.addLink(h2, s2)

  net.start()
  CLI( net )
  net.stop()

if __name__ == '__main__':
  setLogLevel( 'debug' )
  ovsns()

