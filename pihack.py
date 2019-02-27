from optparse import OptionParser
import sys
import urllib2

"""
	api hacker target script by Ms.ambari
	github: https://github.com/Ranginang67
	YouTube: Ms.ambari
"""

def req(target):
	r = urllib2.urlopen(target).read()
	return r

usage = "USAGE: "+sys.argv[0]+" [option]"
objek = OptionParser(usage)
objek.add_option("-t","--traceroute",
				 help="Traceroute Using MTR",action="store_true")
objek.add_option("-d","--dnslookup",
				 help="DNS Lookup",action="store_true")
objek.add_option("-r","--reversedns",
				 help="Reverse dns lookup",action="store_true")
objek.add_option("-f","--findshared",
				 help="find shared dns server",action="store_true")
objek.add_option("-z","--zonetransfer",
				 help="zone transfer",action="store_true")
objek.add_option("-w","--whoislookup",
				 help="Whois lookup",action="store_true")
objek.add_option("-p","--pagelink",
				 help="page link, extract link from page",action="store_true")
objek.add_option("-a","--aslookup",
				 help="autonomous system lookup (AS / ASN / IP)",action="store_true")

(options, args) = objek.parse_args()
if options.traceroute:
	try:
		print req("https://api.hackertarget.com/mtr/?q="+sys.argv[2])
	except:
		pass
elif options.dnslookup:
	try:
		print req("https://api.hackertarget.com/dnslookup/?q="+sys.argv[2])
	except:
		pass
elif options.reversedns:
	try:
		print req("https://api.hackertarget.com/reversedns/?q="+sys.argv[2])
	except:
		pass
elif options.findshared:
	try:
		print req("https://api.hackertarget.com/findshareddns/?q="+sys.argv[2])
	except:
		pass
elif options.zonetransfer:
	try:
		print req("https://api.hackertarget.com/zonetransfer/?q="+sys.argv[2])
	except:
		pass
elif options.whoislookup:
	try:
		print req("https://api.hackertarget.com/whois/?q="+sys.argv[2])
	except:
		pass
elif options.pagelink:
	try:
		print req("https://api.hackertarget.com/pagelinks/?q="+sys.argv[2])
	except:
		pass
elif options.aslookup:
	try:
		print req("https://api.hackertarget.com/aslookup/?q="+sys.argv[2])
	except:
		pass
else:
	print "Try: "+sys.argv[0]+" -h"
