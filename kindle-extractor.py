import html2text
import unidecode
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True,
	help="File to parse")
ap.add_argument("-t", "--test", required=False, default=False,
	help="Test mode")
args = vars(ap.parse_args())

print "Parsing %s" % args["file"]

h = html2text.HTML2Text()

fp = open(args["file"])
data = fp.read()
gooddata = unidecode.unidecode(data.decode("utf-8"))

outfp = open(args["file"].split(".")[0] + ".md", "w")
outfp.write(h.handle(gooddata))