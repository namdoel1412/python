import requests

r = requests.get("http://ip-api.com/json")

#request: https://toidicode.com/?post_id=135

print(r.apparent_encoding)
# print(r.content)
print(r.encoding)
print(r.cookies)
print(r.elapsed)
print(r.encoding)
print(r.headers)
print(r.history)
print(r.is_permanent_redirect)
print(r.iter_content())
print(r.links)
print(r.raise_for_status())
print(r.json())