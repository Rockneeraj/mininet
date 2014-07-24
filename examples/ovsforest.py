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
  r0 = net.addSwitch('r0')
  s1 = net.addSwitch('s1')
  s2 = net.addSwitch('s2')
#  c0 = net.addController('c20')

  net.addLink(r0, s1)
  net.addLink(h1, s1)
  net.addLink(r0, s2)
  net.addLink(h2, s2)

  net.start()
  s1.cmd ('ovs-vsctl set-controller "s1" tcp:10.0.17.23:6653')
  s2.cmd ('ovs-vsctl set-controller "s2" tcp:10.0.17.23:6653')
  
  s1.cmd ('export OVS_RUNDIR=/tmp/mininet-s1/;/virtual-network-platform/virtual_network_agent/virtual_network_agent  --log-file=/var/log/virtual_network_agent1.log --config-file=/virtual-network-platform/virtual_network_agent/tunnel_endpoint_configure.yml --debug;ps -eaf; env')
  #a = 'cp /virtual-network-platform/virtual_network_agent/tunnel_endpoint_configure1.yml tunnel_endpoint_configure.yml'
  #print a 
  #quietRun ( 'cp /virtual-network-platform/virtual_network_agent/tunnel_endpoint_configure1.yml /virtual-network-platform/virtual_network_agent/tunnel_endpoint_configure.yml' )
  s2.cmd ('export OVS_RUNDIR=/tmp/mininet-s2/;/virtual-network-platform/virtual_network_agent/virtual_network_agent --log-file=/var/log/virtual_network_agent2.log --config-file=/virtual-network-platform/virtual_network_agent/tunnel_endpoint_configure1.yml --debug;ps -eaf; env')
  CLI( net )
  net.stop()

if __name__ == '__main__':
  setLogLevel( 'debug' )
  ovsns()

