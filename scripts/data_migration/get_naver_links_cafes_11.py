import urllib.request
import urllib.parse
import re
import json
import time

cafes = [
    "수원 권선 위크위크 리뷰", "부산 베이크백 리뷰", "강남 인터랙트 글루텐프리 리뷰",
    "베통 성수 리뷰", "이태원 키에리 리뷰", "송파 111 OCIC 리뷰",
    "덕수궁 리에제와플 리뷰", "광화문 커피원 리뷰", "신세계백화점 스위트파크 디저트 리뷰",
    "동탄 디스쿱 리뷰"
]

results = {}

for c in cafes:
    print(f"Searching Naver for {c}...")
    try:
        q = urllib.parse.quote(c)
        req = urllib.request.Request(f"https://search.naver.com/search.naver?query={q}", headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        links = list(set(re.findall(r'href="(https://blog\.naver\.com/[^"]+)"', html)))
        clean_links = [l for l in links if "PostView.naver" in l or "PostList.naver" not in l]
        
        results[c] = clean_links[:3]
    except Exception as e:
        print(f"Error for {c}: {e}")
        results[c] = []
    time.sleep(1)

with open("naver_links_cafes_131_140.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Saved to naver_links_cafes_131_140.json")
