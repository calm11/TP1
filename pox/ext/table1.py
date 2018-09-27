#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

"""
TODO: update this so that it reproduces table 1
Can use networkx python library or possibly the mininet plotting,
which looks to be based off of networkx:
https://github.com/mininet/mininet-util/blob/master/plot.py
"""

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('s1')
        # Python's range(N) generates 0..N-1
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)

def simpleTest():
    "Cria e testa uma rede simples"
    topo = SingleSwitchTopo(n=4)
    net = Mininet(topo)
    net.start()
    print "Descarregando conexoes"
    dumpNodeConnections(net.hosts)
    print "Testando conectividade da rede"
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    # Diz para o Mininet imprimir informacoes
    setLogLevel('info')
    simpleTest()
