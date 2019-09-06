import pandas as pd
import codecs

xd = pd.ExcelFile('C:\\report.xls')
df = xd.parse()
with codecs.open('C:\\report.html', 'w', 'utf-8') as html_file:
    html_file.write(df.to_html(header=True, index=False))
