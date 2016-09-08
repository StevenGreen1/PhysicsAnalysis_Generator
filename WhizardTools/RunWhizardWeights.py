#!/usr/bin/env python

import os, sys, re, subprocess
from os import environ
from subprocess import Popen, PIPE

#=====================================================================================
# Helper Function
#=====================================================================================

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump

#=====================================================================================
# Main
#=====================================================================================

# Inputs
whizardJobSet = int(sys.argv[1])
process = 'ee_nunuqqqq'
energy = 1400

# Set up directories
whizardHomeDirectory = '/usera/sg568/Whizard_v1-97/whizard-1.97/results'
whizardDirectory = '/r06/lc/sg568/PhysicsAnalysis/Generator/' + process + '/' + str(energy) + 'GeV/WhizardJobSet' + str(whizardJobSet)
whizardInputTemplate = os.path.join(whizardHomeDirectory, 'BatchWeightsWhizard.in')
whizardMdlFile = os.path.join(whizardHomeDirectory,'whizard')

# Get template content
whizardInputFileTemplate = open(whizardInputTemplate,'r')
whizardInputTemplateContent = whizardInputFileTemplate.read()
whizardInputFileTemplate.close()

# Modify template to Whizard Job Set variable 
whizardFilename = 'WhizardJobSet' + str(whizardJobSet)
whizardInputTemplateContent = re.sub('#Directory#', whizardDirectory, whizardInputTemplateContent)
whizardInputTemplateContent = re.sub('#Filename#', whizardFilename, whizardInputTemplateContent)
whizardInputTemplateContent = re.sub('#WhizardMdlFile#', whizardMdlFile, whizardInputTemplateContent)
whizardInputTemplateContent = re.sub('#NEvents#', '10000', whizardInputTemplateContent)
whizardInputTemplateContent = re.sub('#RandomSeed#', str(whizardJobSet), whizardInputTemplateContent)

# Set up environment 
os.chdir(whizardDirectory)
os.environ["DEBUSSY"] = "1"
os.environ["LUMI_LINKER"] = "/usera/sg568/PhysicsAnalysis/Generator/BeamSprectra/beam_spectraV7/lumi_linker_000"
os.environ["PHOTONS_B1"] = "/usera/sg568/PhysicsAnalysis/Generator/BeamSprectra/beam_spectraV7/photons_beam1_linker_000"
os.environ["PHOTONS_B2"] = "/usera/sg568/PhysicsAnalysis/Generator/BeamSprectra/beam_spectraV7/photons_beam2_linker_000"
os.environ["EBEAM"] = "/usera/sg568/PhysicsAnalysis/Generator/BeamSprectra/beam_spectraV7/ebeam_in_linker_000"
os.environ["PBEAM"] = "/usera/sg568/PhysicsAnalysis/Generator/BeamSprectra/beam_spectraV7/pbeam_in_linker_000"
os.environ["LUMI_EE_LINKER"] = "/usera/sg568/PhysicsAnalysis/Generator/BeamSprectra/beam_spectraV7/lumi_ee_linker_000"
os.environ["LUMI_EG_LINKER"] = "/usera/sg568/PhysicsAnalysis/Generator/BeamSprectra/beam_spectraV7/lumi_eg_linker_000"
os.environ["LUMI_GE_LINKER"] = "/usera/sg568/PhysicsAnalysis/Generator/BeamSprectra/beam_spectraV7/lumi_ge_linker_000"
os.environ["LUMI_GG_LINKER"] = "/usera/sg568/PhysicsAnalysis/Generator/BeamSprectra/beam_spectraV7/lumi_gg_linker_000"

# Make copy of stdhep settings
stdhepFolder = 'UploadedFiles'
copyFilesCommand = 'cp whizard.*.evx ' + stdhepFolder
subprocess.Popen(copyFilesCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
subprocess.call(['cp', 'whizard.in', stdhepFolder])
subprocess.call(['cp', 'WhizardJobSet' + str(whizardJobSet) + '.vvqqqq.out',stdhepFolder])

# Loop over weights
for alpha4 in frange(-0.05, 0.05, 0.01):
    for alpha5 in frange(-0.05, 0.05, 0.01):
        activeWhizardInputContent = whizardInputTemplateContent
        activeWhizardInputContent = re.sub('#Alpha4#','%.5f' % alpha4, activeWhizardInputContent)
        activeWhizardInputContent = re.sub('#Alpha5#','%.5f' % alpha5, activeWhizardInputContent)
        whizardInputFileActive = os.path.join(whizardDirectory, 'whizard.in')

        file = open(whizardInputFileActive,'w')
        file.write(activeWhizardInputContent)
        file.close()

        runWhizard = Popen('./whizard', shell=True) #stdout=PIPE, shell=True)
        runWhizard.wait()

        resultsFolder = os.path.join(whizardDirectory,'Alpha4_%.5f_Alpha5_%.5f' % (alpha4,alpha5))
        if not os.path.exists(resultsFolder):
            os.makedirs(resultsFolder)

        copyFilesCommand = 'cp WhizardJobSet' + str(whizardJobSet) + '.*.evt ' + resultsFolder
        subprocess.Popen(copyFilesCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.call(['cp','whizard.in',resultsFolder])
        subprocess.call(['cp', 'WhizardJobSet' + str(whizardJobSet) + '.out',resultsFolder])
