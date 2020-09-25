import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))

outputs = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	outputs.addPage(page)

	with open('watermarked_output.pdf', 'wb') as file:
		outputs.write(file)













'''
a program to merge many pdf files
'''

import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('super.pdf')
pdf_combiner(inputs)



'''
How to grab a file . read it(rb read binary)
rotate the page, and write a new page

'''


with open('dummy.pdf', 'rb') as file:
	reader = PyPDF2.PdfFileReader(file)
	page = reader.getPage(0)
	page.rotateCounterClockwise(90)
	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page)
	with open ('tilt.pdf', 'wb') as new_file:
		writer.write(new_file)