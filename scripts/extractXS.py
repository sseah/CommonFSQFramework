#! /usr/bin/env python

import os, json

def fetchData(linkBase, minI, maxI):
    oFile = "/tmp/someCrazyNameNoOneWillSuspectWookieSchonShonStarWars.json"
    for i in xrange (minI, maxI):
        lenOfNum = len(str(i))
        numberOfZeros = 5-lenOfNum
        numString = "0"*numberOfZeros+str(i)
        link = linkBase+numString
        #print link
        os.system("rm " + oFile)
        command = "wget --no-check-certificate " + link + " -O " + oFile + " -q"
        os.system(command)

        with open(oFile,"r") as f:
            myJson = json.load(f)

            dsName = myJson[u'results'][u'dataset_name']
            if len(myJson[u'results'][u'generator_parameters']) != 1:
                print "Problem with", dsName
                continue
            xs = float(myJson[u'results'][u'generator_parameters'][0][u'cross_section'])
            matchE = float(myJson[u'results'][u'generator_parameters'][0][u'match_efficiency'])
            filterE = float(myJson[u'results'][u'generator_parameters'][0][u'filter_efficiency'])

            #print dsName, xs, matchE, filterE
            r1 = matchE/1.
            r2 = filterE/1.
            if r1 < 0.999 or r1 > 1.001:
                print "Dont know what to do whith match efficiency", matchE,
                print "   -> skipping " + dsName
                continue
            if r2 < 0.999 or r2 > 1.001:
                print "Dont know what to do whith filter efficiency", filterE,
                print "   -> skipping " + dsName
                continue
            print '    s["' + dsName + '"] = ' + str(xs) + " # " + link

            #for e in myJson[u'results']:
            #    print e, type(e)


if __name__ == "__main__":
    #fetchData("https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/BTV-Fall13-", 29, 53)
    fetchData("https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get/FSQ-Fall13-", 1, 26)


