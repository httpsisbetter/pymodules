import urllib.request

def urllib_curl(target):
    try:
        response = urllib.request.urlopen(target)
        print("[+] " + target + " " + "Response code: " + str(response.getcode()))
    except urllib.error.URLError as error:
        print("[-] Unable to curl " + str(target) + ": " + str(error.reason))
    except urllib.error.HTTPError as error:
        print("[-] Unable to curl " + str(target) + ": " + str(error.reason))
    except ValueError as error:
        print("[-] Unable to curl " + str(target) + ": " + str(error))
