import urllib.request
import urllib.parse
import re
import json
import time

cafes = [
    "강남 베이커스트 브라운 리뷰", "동탄 고페르 카페 리뷰", "대전 흐그이므자 카페 리뷰",
    "성남 버터브루 카페 리뷰", "문정 아이스걸크림보이 리뷰", "성남 웰로우 카페 리뷰",
    "성남 멜리플리 카페 리뷰", "송파 니드스윗 리뷰", "동탄 로텐바우 카페 리뷰"
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

with open("naver_links_cafes_112_120.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Saved to naver_links_cafes_112_120.json")
