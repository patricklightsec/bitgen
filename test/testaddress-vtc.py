#!/usr/bin/python

import os
import sys
import os.path

def printHeader(str) :
   "Prints header text"
   print "===================== " + str + " ====================="
   return

if not os.path.isfile("../bitgen-vtc"):
	print "Error, application binary does not exist"
	sys.exit()




#============ Start of tests ============

printHeader("Test 1 bitgen-vtc info")
retval1 = os.system("../bitgen-vtc info WUo1dSAmJHU7MUXftUcf6S535F4w4J59wB3bFToRWWuLCuUhUf9S")
if retval1 != 0:
	print "test 1 error"
	sys.exit()

printHeader("Test 2 bitgen-vtc info err")
retval1 = os.system("../bitgen-vtc info WUo1dSAmrrrrrrrrrrrrrrrrrrrw4J59wB3bFToRWWuLCuUhUf9S")
if retval1 == 0:
	print "test 2 error"
	sys.exit()


printHeader("Test 3 bitgen-vtc info")
retval1 = os.system("../bitgen-vtc info Vvehgm6WvbfEsAUb5J4VBZ3D4YmyW7dVTo")
if retval1 != 0:
	print "test 3 error"
	sys.exit()

printHeader("Test 4 bitgen-vtc info err")
retval1 = os.system("../bitgen-vtc info VvehgiiiiiiiiiiiiiiiiZ3D4YmyW7dVTo")
if retval1 == 0:
	print "test 4 error"
	sys.exit()



printHeader("Test 5 bitgen-vtc hash")
retval1 = os.system("../bitgen-vtc hash kdfdksjdhfjksdhfjhdsjfhjdhfjhkfjsdjjjdjjdjdjdjjdsjfdkfjhsdkfjhsdfkjhsdkfjhsdkjfhskjdhfsadjhasdkhaskdjhaksjdhkjhjhhhhfhfhjdjjjdjjdjdjjdsadjalskdjaslkjdalksjdlaksjdlkasjdlaksjdlkasjdlkasjdlaksjdlkasjdasdasda nops nocounter")
if retval1 != 0:
	print "test 5 error"
	sys.exit()


if not os.path.isfile("vtc_address_Vw56P3ejcYEvpi26i2RFB29oCKJ3rac7mf_private.txt"):
	print "test 5 file error"
	sys.exit()



printHeader("Test 6 bitgen-vtc hdice")
retval1 = os.system("../bitgen-vtc dice 6126361236126312635353526351263512635162536125361253612536125312312312312312312312312312312321332131 nops nocounter")
if retval1 != 0:
	print "test 6 error"
	sys.exit()


if not os.path.isfile("vtc_address_Vtqgb6ZLdbVAvnu4ShmtG6Dvc7iqtPycLU_private.txt"):
	print "test 6 file error"
	sys.exit()



printHeader("Test 7 bitgen-vtc hex")
retval1 = os.system("../bitgen-vtc hex 116161678ABCDEFEFA1231231236127327633764736473643434342343423444 nops nocounter")
if retval1 != 0:
	print "test 7 error"
	sys.exit()


if not os.path.isfile("vtc_address_VkeebAvKbMGoxF53zzwLwGBeL4WYYFQBEe_private.txt"):
	print "test 7 file error"
	sys.exit()



printHeader("Test 8 bitgen-vtc hex compressed")
retval1 = os.system("../bitgen-vtc hex 116161678ABCDEFEFA1231231236127327633764736473643434342343423417 compressed nops nocounter")
if retval1 != 0:
	print "test 8 error"
	sys.exit()


if not os.path.isfile("vtc_address_Vqwt1djeEPBpJtCsFs4xYgdBmgVUPoWz2K_private.txt"):
	print "test 8 file error"
	sys.exit()


printHeader("Test 9 bitgen-vtc mnemonic")
retval1 = os.system("../bitgen-vtc mnemonic \"nice upset area coconut emerge swim tomorrow hospital luggage mushroom abuse odor color early bicycle slow cart lamp gas lawn lava cancel insane amused\" nops nocounter")
if retval1 != 0:
	print "test 9 error"
	sys.exit()


if not os.path.isfile("vtc_address_VeYT9Jj64HA6c12oqm5FGkAXzsLjbGX6z3_private.txt"):
	print "test 9 file error"
	sys.exit()


printHeader("Test 10 bitgen-vtc wif")
retval1 = os.system("../bitgen-vtc wif WXfiEF24RbcPPkvTE4T38mZ9dDwUt4HWLmMEjjKugM9nUmUCDPCi nops nocounter")
if retval1 != 0:
	print "test 10 error"
	sys.exit()


if not os.path.isfile("vtc_address_VpBejPDYzdwk1oUJw3ZYvWkVTY5SD5Yk4q_private.txt"):
	print "test 10 file error"
	sys.exit()


printHeader("Test 11 bitgen-vtc mnemonic")
retval1 = os.system("../bitgen-vtc brainwallet mysalt@test.com \"This is the rather long passphrase that is used tO tEst thiS thing so we know that iit is workingg CorrectlY\" nops nocounter")
if retval1 != 0:
	print "test 11 error"
	sys.exit()


if not os.path.isfile("vtc_address_VjwYuLt8CZNpyJaZ2HQ4j8ppfR2NVwPRVW_private.txt"):
	print "test 11 file error"
	sys.exit()


print ""
print ""
print ""
print "Cleaning up"
os.system("rm *.trans *.script *.txt *.sig")

print ""
print ""
print ""
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
print "++++++++++++++++++++++++++++++ All tests passed OK +++++++++++++++++++++++++++"
print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"


sys.exit(123)
