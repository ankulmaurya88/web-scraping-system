# # BeautifulSoup parsing logic
# from bs4 import BeautifulSoup

# def parse_with_bs(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     return {'title': soup.title.string if soup.title else None}



# from bs4 import BeautifulSoup
# from output_handler.save import save_output_row_text
# # bs_parser/parser.py
# from bs4 import BeautifulSoup

# def parse_with_bs(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     result = {}
#      # Print all visible text content (raw readable text)



    
#     print("=== Full Page Text ===")
#     text_data = soup.get_text(separator=' ', strip=True)
#     # print(text_data)  # <- This prints everything readable
#     # result['full_text'] = text_data
#     # print(soup.get_text())  # <- This prints everything readable
#     # save_output_row_text(text_data)

#     # print (text_data)
#     # Example: extract all text within <h1> tags
#     result['titles'] = [h1.get_text(strip=True) for h1 in soup.find_all('h1')]
#     # print("=== Titles ===")
#     # print(result['titles'])  # <- This prints all titles found
#     # Example: extract all hyperlinks
#     result['links'] = [a['href'] for a in soup.find_all('a', href=True)]

#     # print("=== Links ===")
#     # print(result['links'])

#     # save_output(text_data)
#     # print("=== Paragraphs ===")
#     result['paragraphs'] = [p.get_text(strip=True) for p in soup.find_all('p')]
#     # print(result['paragraphs'])  # <- This prints all paragraphs found
#     # print(result)
#     return result













from unittest import result
from bs4 import BeautifulSoup
from collections import defaultdict


from output_handler.save import OutputSaver




def parse_with_bs(html):
    soup = BeautifulSoup(html, 'html.parser')
    return parse_using_heuristics(soup)



def parse_using_heuristics(soup: BeautifulSoup):
    result = defaultdict(list)

    # ---------- Titles ----------
    for i in range(1, 7):
        tags = soup.find_all(f'h{i}')
        for tag in tags:
            text = tag.get_text(strip=True)
            print(text)
            if text:
                result['titles'].append(text)

    # ---------- Paragraphs ----------
    for p in soup.find_all('p'):
        text = p.get_text(strip=True)
        if len(text) > 30:  # Filter out short/noisy content
            result['paragraphs'].append(text)

    # ---------- Lists ----------
    for ul in soup.find_all(['ul', 'ol']):
        items = [li.get_text(strip=True) for li in ul.find_all('li') if li.get_text(strip=True)]
        if items:
            result['lists'].append(items)

    # ---------- Links ----------
    for a in soup.find_all('a', href=True):
        text = a.get_text(strip=True)
        href = a['href']
        if text and href and not href.startswith('#'):
            result['links'].append({'text': text, 'href': href})

    # ---------- Tables ----------
    for table in soup.find_all('table'):
        rows = []
        for tr in table.find_all('tr'):
            cols = [td.get_text(strip=True) for td in tr.find_all(['td', 'th']) if td.get_text(strip=True)]
            if cols:
                rows.append(cols)
        if rows:
            result['tables'].append(rows)

    # ---------- Metadata ----------
    for meta in soup.find_all('meta'):
        name = meta.get('name') or meta.get('property')
        content = meta.get('content')
        if name and content:
            result['meta'].append({name: content})

    # ---------- Class-based content blocks ----------
    important_classes = ['main', 'content', 'article', 'body', 'entry-content', 'post', 'text', 'description']
    for class_name in important_classes:
        for div in soup.find_all(['div', 'section', 'article'], class_=lambda x: x and class_name in x.lower()):
            text = div.get_text(separator=' ', strip=True)
            if len(text) > 100 and text not in result['paragraphs']:  # Avoid duplicates
                result['content_blocks'].append(text)

    # ---------- Fallback Full Text ----------
    all_text = soup.get_text(separator=' ', strip=True)
    if not result['paragraphs'] and len(all_text) > 100:
        result['full_text'] = all_text

    # return dict(result)
    return result




