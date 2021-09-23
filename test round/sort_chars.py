import json

from requests import get

url: str = input()
port: int = int(input())
a: int = int(input())
b: int = int(input())

res = json.loads(get(f"{url}:{port}?a={a}&b={b}").text)
print("\n".join(map(str, filter(lambda x: x > 0, sorted(res, reverse=True)))))
