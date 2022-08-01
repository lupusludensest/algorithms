import fitz

file_name = 'E:\Gurov_SSD_256\My_docs\CV\Deloitte_dt_28_April_2021\Viacheslav_Gurov_-_Viacheslav_Gurov_EH_Offer_Deloitte_dt_28_apr_2021.pdf'
search_term = 'Deloitte'
pdf = fitz.open(file_name)

for current_page in range(len(pdf)):
    page = pdf.load_page(current_page)

    if page.search_for(search_term):
        print(f'Word "{search_term}" found on "{current_page} page"')