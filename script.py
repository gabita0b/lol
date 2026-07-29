from datasets import load_dataset
from bs4 import BeautifulSoup
import collections, json
from tqdm import tqdm

# Load dataset (html config) and process entries
print('Loading dataset...')
ds = load_dataset('stanforddams/daily','html', split='train')

records = []
for ex in tqdm(ds, desc='processing'):
    html = ex.get('html','') or ''
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text(' ', strip=True)
    title = soup.title.string if soup.title else ''
    li_count = html.count('<li>')
    records.append({'title': title, 'text': text, 'li_count': li_count})

n = len(records)
avg_li = sum(r['li_count'] for r in records)/n if n else 0

keywords = ['bike','vehicle burglary','petty theft','grand theft','arson','assault','battery','extortion','hit and run','stalking','drugs','vandalism','loitering','burglary','theft','rape']
counts = collections.Counter()
for r in records:
    t = r['text'].lower()
    for k in keywords:
        counts[k] += t.count(k)

out = {
    'n_posts': n,
    'avg_incidents_per_post_approx': avg_li,
    'keyword_counts': counts.most_common(20),
    'sample_posts': [
        {'title': records[i]['title'], 'excerpt': records[i]['text'][:300], 'li_count': records[i]['li_count']} for i in range(min(5,n))
    ]
}

# Print and save
print(json.dumps(out, ensure_ascii=False, indent=2))
with open('eda_output.json','w', encoding='utf8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print('\nSaved EDA results to eda_output.json')
