import whois

def get_whois_org(target):
    try:
        w = whois.whois(target)
        print("[+] Whois data for " + str(target) + ":")
        print("Org: " + w.org)
        print("Country: " + w.country)
    except Exception as e:
        print("[-] Unable to retrieve whois data for " + str(target))


