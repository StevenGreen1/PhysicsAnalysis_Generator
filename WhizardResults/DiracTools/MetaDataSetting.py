import os

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

jobDescription = 'StdHep'

eventsToSimulate = [ { 'Process': 'ee_nunuww_nunuqqqq', 'Energies': [1400] } ]

fc = FileCatalogClient()

for eventSelection in eventsToSimulate:
    process = eventSelection['Process']
    for energy in eventSelection['Energies']:
        path = '/ilc/user/s/sgreen/PhysicsAnalysis/StdHep/' + process + '/' + str(energy) + 'GeV'
        pathdict = {'path':path, 'meta':{'JobDescription':jobDescription,'EvtType':process,'Energy':energy}}
        res = fc.setMetadata(pathdict['path'], pathdict['meta'])
