import requests

url = "https://api.github.com/repos/easternslope/test/contents/test1/demo10.txt"

payload = "{\n  \"message\": \"my commit message\",\n  \"committer\": {\n    \"name\": \"xxxxxx\",\n    \"email\": " \
          "\"xxxxxx@sssss.com\"\n  },\n  \"content\": \"bXkgdXBkYXRlZCBmaWxlIGNvbnRlbnRz\",\n  \"sha\": " \
          "\"329688480d39049927147c162b9d2deaf885005f\"\n} "
headers = {
    'authorization': "token xxxxxxxxxxxxxxxxxxxxxxxxxx",
    'cache-control': "no-cache",
    'postman-token': "cd745ed3-5f4e-9292-930c-c32451fb7593"
    }
print(payload)
print('')
print(headers)
response = requests.request("PUT", url, data=payload, headers=headers)

print(response.text)