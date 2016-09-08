#!/usr/bin/python

import os, sys, getopt, re, subprocess, math, dircache, logging, time, random, string

class CondorWhizard:
    'Common base class for running whizard on condor'

### ----------------------------------------------------------------------------------------------------
### Start of constructor
### ----------------------------------------------------------------------------------------------------

    def __init__(self):

        self._WhizardArgList = [] 
        self._ExecutableName = 'RunWhizard.py'
        self._Executable = os.path.join('/var/clus/usera/sg568/Whizard_v1-97/whizard-1.97/results/BatchJobs', self._ExecutableName)
        self._CondorMaxRuns = 75

        for i in range(1,12):
            self._WhizardArgList.append(str(i))

        self.runCondorJobs()
        self.checkCondorJobs()

### ----------------------------------------------------------------------------------------------------
### Start of runCondorJobs function
### ----------------------------------------------------------------------------------------------------

    def runCondorJobs(self):
        nQueued = self.nQueuedCondorJobs()
        condorJobFile = 'Whizard.job'

        while True:
            for idx, fileToRun in enumerate(self._WhizardArgList):
                nRemaining = len(self._WhizardArgList) - idx - 1
                nQueued = 0 

                while True:
                    nQueued = self.nQueuedCondorJobs()
                    if nQueued >= self._CondorMaxRuns:
                        time.sleep(10)
                    else:
                        break

                with open(condorJobFile, 'w') as jobFile:
                    jobString = self.getCondorJobString()
                    jobString += 'arguments = ' + fileToRun + '\n'
                    jobString += 'queue 1 \n'
                    jobFile.write(jobString)

                subprocess.call(['condor_submit', condorJobFile])
                print 'Submitted job as there were only ' + str(nQueued) + ' jobs in the queue and ' + str(nRemaining) + ' jobs remaining.'
                time.sleep(0.5)
                os.remove(condorJobFile)

                if 0 == nRemaining:
                    print 'All condor jobs submitted.'
                    return

### ----------------------------------------------------------------------------------------------------
### End of runCondorJobs function
### ----------------------------------------------------------------------------------------------------
### Start of getCondorJobString function
### ----------------------------------------------------------------------------------------------------

    def getCondorJobString(self):
        jobString  = 'executable              = ' + self._Executable + '                                             \n'
        jobString += 'initial_dir             = ' + os.getcwd() + '                                                  \n'
        jobString += 'notification            = never                                                                \n'
        jobString += 'Requirements            = (OSTYPE == \"SLC6\")                                                 \n'
        jobString += 'Rank                    = memory                                                               \n'
        jobString += 'output                  = ' + os.environ['HOME'] + '/CondorLogs/Whizard.out                    \n'
        jobString += 'error                   = ' + os.environ['HOME'] + '/CondorLogs/Whizard.err                    \n'
        jobString += 'log                     = ' + os.environ['HOME'] + '/CondorLogs/Whizard.log                    \n'
        jobString += 'environment             = CONDOR_JOB=true                                                      \n'
        jobString += 'Universe                = vanilla                                                              \n'
        jobString += 'getenv                  = false                                                                \n'
        jobString += 'copy_to_spool           = true                                                                 \n'
        jobString += 'should_transfer_files   = yes                                                                  \n'
        jobString += 'when_to_transfer_output = on_exit_or_evict                                                     \n'
        return jobString

### ----------------------------------------------------------------------------------------------------
### End of getCondorJobString function
### ----------------------------------------------------------------------------------------------------
### Start of checkCondorJobs function
### ----------------------------------------------------------------------------------------------------

    def checkCondorJobs(self):
        while True:
            nActiveJobs = self.nQueuedCondorJobs()
            print 'There are ' + str(nActiveJobs) + ' jobs running on condor.'
            if (nActiveJobs > 0):
                time.sleep(10)
            else:
                print 'There are no more active condor jobs.'
                return

### ----------------------------------------------------------------------------------------------------
### End of checkCondorJobs function
### ----------------------------------------------------------------------------------------------------
### Start of nQueuedCondorJobs function
### ----------------------------------------------------------------------------------------------------

    def nQueuedCondorJobs(self):
        queueProcess = subprocess.Popen(['condor_q','-w'], stdout=subprocess.PIPE)
        queueOutput = queueProcess.communicate()[0]
        regex = re.compile(self._ExecutableName)
        queueList = regex.findall(queueOutput)
        return int(len(queueList))

### ----------------------------------------------------------------------------------------------------
### End of nQueuedCondorJobs function
### ----------------------------------------------------------------------------------------------------

### ----------------------------------------------------------------------------------------------------
### Call class in main
### ----------------------------------------------------------------------------------------------------
CondorWhizard()
