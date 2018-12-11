from win32com import client

w = client.Dispatch("Word.Application")
doc = w.Documents.Open('d:\\temp\\b.docx')
doc.ExportAsFixedFormat('D:\\temp\\word.pdf', client.constants.wdExportFormatPDF)
w.Quit()
