import pypdf
import os

merger = pypdf.PdfMerger()

for file in os.listdir(os.curdir):
    try:
        pdf = pypdf.PdfReader(file)
    except:
        continue
    
    merger.append(file)
    merger.write("combinedPDFfiles.pdf")