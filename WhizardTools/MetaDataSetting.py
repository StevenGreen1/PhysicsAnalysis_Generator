import os

from DIRAC.Core.Base import Script
Script.parseCommandLine()
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

jobDescription = 'PhysicsAnalysis'

eventsToSimulate = [ 
                       { 'EventType': 'ee_nunuqqqq'  , 'Energies':  ['3000'] }
                   ]

fc = FileCatalogClient()

for eventSelection in eventsToSimulate:
    process = eventSelection['EventType']
    for energy in eventSelection['Energies']:
        path = '/ilc/user/s/sgreen/' + jobDescription + '/StdHep/' + process + '/' + str(energy) + 'GeV' 
        pathdict = {'path':path, 'meta':{'Energy':energy, 'EvtType':process, 'JobDescription':jobDescription}}
        res = fc.setMetadata(pathdict['path'], pathdict['meta'])

