#!/usr/bin/env python

import os, sys, re, subprocess
from os import environ
from subprocess import Popen, PIPE

#=====================================================================================

whizardJobSet = int(sys.argv[1])
process = 'ee_nunuqqqq'
energy = 1400

whizardHomeDirectory = '/usera/sg568/Whizard_v1-97/whizard-1.97/results'
#whizardDirectory = '/usera/sg568/Whizard_v1-97/whizard-1.97/results/BatchJobs/WhizardJobSet' + str(whizardJobSet)
whizardDirectory = '/r06/lc/sg568/PhysicsAnalysis/Generator/' + process + '/' + str(energy) + 'GeV/StdHep/WhizardJobSet' + str(whizardJobSet)

if not os.path.exists(whizardDirectory):
    os.makedirs(whizardDirectory)

whizardExecutable = os.path.join(whizardHomeDirectory, 'whizard')
os.system('cp ' + whizardExecutable + ' ' + whizardDirectory)
whizardExecutable = os.path.join(whizardDirectory, 'whizard')

whizardInputTemplate = os.path.join(whizardHomeDirectory, 'BatchStdhepWhizard.in')
whizardMdlFile = '/usera/sg568/Whizard_v1-97/whizard-1.97/results/whizard'

whizardInputFileTemplate = open(whizardInputTemplate,'r')
whizardInputTemplateContent = whizardInputFileTemplate.read()
whizardInputFileTemplate.close()

whizardFilename = 'WhizardJobSet' + str(whizardJobSet)

whizardInputTemplateContent = re.sub('#Directory#', whizardDirectory, whizardInputTemplateContent)
whizardInputTemplateContent = re.sub('#Filename#', whizardFilename, whizardInputTemplateContent)
whizardInputTemplateContent = re.sub('#WhizardMdlFile#', whizardMdlFile, whizardInputTemplateContent)
whizardInputTemplateContent = re.sub('#NEvents#', '10000', whizardInputTemplateContent)
whizardInputTemplateContent = re.sub('#RandomSeed#', str(whizardJobSet), whizardInputTemplateContent)

whizardInputFileActive = os.path.join(whizardDirectory, 'whizard.in')

file = open(whizardInputFileActive,'w')
file.write(whizardInputTemplateContent)
file.close()

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

runWhizard = Popen('./whizard', shell=True) #stdout=PIPE, shell=True)
runWhizard.wait()

#=====================================================================================

"""
 &process_input
 input_file = ""
 process_id = "vvqqqq"
 sqrts = 1400
 polarized_beams = T
 structured_beams = T
 beam_recoil = T
!luminosity = 0
 /

 &integration_input
 calls =
   1  20000
  10  20000
   1  100000
! calls =
!   1  200000
!  10  200000
!   1  500000
 seed = 123456
!  Read grids or not. If not, integration will be done
 read_grids = F
 read_grids_force = F
 default_mass_cut = 4.
 default_q_cut = 4.
! phase_space_only = T
 /

 &simulation_input
 keep_beam_remnants = T
 keep_initials = T
 events_per_file = 1000
 fragment = F
 fragmentation_method = 3
 pythia_parameters = "PMAS(25,1)=125.0; PMAS(25,2)=0.3605E-02; MSTU(22)=20; MSTJ(28)=2; PARJ(21)=0.40000;PARJ(41)=0.11000; PARJ(42)=0.52000; PARJ(81)=0.25000; PARJ(82)=1.90000; MSTJ(11)=3; PARJ(54)=-0.03100; PARJ(55)=-0.00200;PARJ(1)=0.08500; PARJ(3)=0.45000; PARJ(4)=0.02500; PARJ(2)=0.31000; PARJ(11)=0.60000; PARJ(12)=0.40000; PARJ(13)=0.72000;PARJ(14)=0.43000; PARJ(15)=0.08000; PARJ(16)=0.08000; PARJ(17)=0.17000; MSTP(3)=1"
!   Make events or not:
 n_events = 350000
 write_events = T
! Write raw events
write_events_raw = F
! Recalculate matrix elements
recalculate = T
! Unweighted
!unweighted = F
!   pythia ascii:
! write_events_format = 11
!   stdhep:
! write_events_format = 20
!   "long" ascii:
 write_events_format = 3
/

 &diagnostics_input
 show_phase_space = F
 screen_histograms=T
 /

 &parameter_input
 me = 0
 mmu = 0.10566
 mtau = 1.77
 ms = 0
 mc = 0.54
 mb = 2.9
 MH = 125.
 wH = 0.3605E-02
 mtop = 174.
 alphas = 0.000001
 a4 = 0.10000
 a5 = 0.10000
/

 &beam_input
 particle_name = 'e1'
 polarization = 0.0 0.0
 USER_spectrum_on = T
 USER_spectrum_mode = 19
 ISR_on = T
 ISR_alpha = 0.0072993
 ISR_m_in = 0.000511
 EPA_on = F
 EPA_alpha = 0.0072993
 EPA_m_in = 0.000511
 EPA_mX = 4.
 EPA_Q_max = 4.
/
 &beam_input
 particle_name = 'E1'
 polarization = 0.0 0.0
 USER_spectrum_on = T
 USER_spectrum_mode = -19
 ISR_on = T
 ISR_alpha = 0.0072993
 ISR_m_in = 0.000511
 EPA_on = F
 EPA_alpha = 0.0072993
 EPA_m_in = 0.000511
 EPA_mX = 4.
 EPA_Q_max = 4.
 /
"""
