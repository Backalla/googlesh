from bs4 import BeautifulSoup

def get_results(html):
    div_soup = BeautifulSoup(html,"html.parser")
    results_texts = []
    results = div_soup.find_all('h3',class_="r")
    for result in results:
        result_heading_text = result.a.text.encode('ascii','ignore')
        results_texts.append(result_heading_text)
    
    return results_texts
