# Open the SLA file passed to Scribus, replace the content of the text frame named "placeholder" with
# the value in the -t argument and produce a PDF file named as defined by the -o argument.
#
# usage:
# - create a SLA file with a text frame named "placeholder"
# - run scribus -g -py to-pdf-with-placeholder.py -pa -o file.pdf -pa -t "welcome to scribus" file.sla

import sys
import getopt
import scribus

# print(sys.argv)

text_usage = "scribus -g -py " + sys.argv[0] + " -pa -o <outputfile.pdf> -pa -t <text place holder> <inputfile.sla>"
pdf_file = ''
text_placeholder = ''

try:
  opts, args = getopt.getopt(sys.argv[2:],"ho:t:",["output=", "text="])
except getopt.GetoptError:
  print(text_usage)
  sys.exit(2)

for opt, arg in opts:
  if opt == "-h":
     print(text_usage)
     sys.exit()
  elif opt in ("-o", "--output"):
     pdf_file = arg
  elif opt in ("-t", "--text"):
     text_placeholder = arg

if (pdf_file == "" or text_placeholder == "") :
     print(text_usage)
     sys.exit()

if scribus.haveDoc() :
    scribus.setText(text_placeholder, "placeholder")
    pdf = scribus.PDFfile()
    pdf.file = pdf_file
    pdf.save()
else :
    print("No file open")
