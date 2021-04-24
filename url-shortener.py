import base64
import webbrowser
import random
import string

# shortening long user defined url into generated short URLs (cybr.xyz0)
# Once the short URL is entered, it is matched in the dictionary and corresponding long url is triggered


def gen_url(chars = string.ascii_lowercase + string.digits, N=4):
	return ''.join(random.choice(chars) for _ in range(N))

gen_url_result = gen_url()

print(" Enter 1 to assign URL manually.\n Enter 2 to use 'https://twitter.com/NatGeo/status/1385598102367780866 ' \n")
temp= input(" Enter choice:  ")
if temp == "1":
    original_url = input(" Enter the URL to be shortened: ") 
if temp == "2":
    original_url = "https://twitter.com/NatGeo/status/1385598102367780866"

print("Original URL is: ", original_url)

o_url_bytes = original_url.encode("ascii")

encoded_bytes = base64.b64encode(o_url_bytes)
encoded_url = encoded_bytes.decode("ascii")

short_url = "cybr."+gen_url_result         # generated URL

print("Generated Short URL: ", short_url)
dict = []
dict.append(original_url)
dict.append(encoded_url)
dict.append(short_url)

#print(dict[0])

new_url = input("Enter Generated short url: ")   
if new_url == short_url:
    webbrowser.open(dict[0])
else:
    print("short url doesnt match records")
