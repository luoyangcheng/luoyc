import comtypes.client


def convertDocxToPDF(infile, outfile):
    wdFormatPDF = 17
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(infile)
    doc.SaveAs(outfile, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()


if __name__ == '__main__':
    convertDocxToPDF('D:\\temp\\b.docx', 'D:\\temp\\bb.pdf')
