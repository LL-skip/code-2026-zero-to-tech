import requests

resp = requests.get("https://api.ipify.org?format=json", timeout=10)
print(resp.json())

try:
    response = requests.get(
        "http://127.0.0.1:1",
        timeout=2
    )
except requests.exceptions.RequestException as e:
    print("发生异常：", type(e).__name__)
    print(e)

try:
    response = requests.get(
        "https://httpbin.org/delay/5",
        timeout=1
    )
except requests.exceptions.RequestException as e:
    print("发生异常：", type(e).__name__)
    print(e)

response = requests.Response()
response.status_code = 404
response.url = "demo://test"

try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("发生 HTTP 异常：", e)

url = "https://api.ipify.org?format=json"
response = requests.get(url, timeout=10)

print(response.status_code)

response.raise_for_status()