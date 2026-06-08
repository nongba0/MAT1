import sys
from bs4 import BeautifulSoup

with open(r'C:\Users\sangw\.gemini\antigravity\brain\b66d6635-7ef1-478d-a0b1-d5a78d2a1413\.system_generated\steps\5516\content.md', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
article = soup.select_one('.tt_article_useless_p_margin')

with open('temp_article.txt', 'w', encoding='utf-8') as f:
    f.write(article.get_text('\n', strip=True) if article else 'Not found')
