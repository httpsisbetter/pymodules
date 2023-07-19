import dns.resolver
import socket

# MX lookup
def mx_lookup(target):
    try:
        for result in dns.resolver.query(target, 'MX'):
            print("[+] " + target + ": " + result.to_text())
    except Exception as e:
        print("[-] " + target + ": " + "Unable to resolve")

# DNS lookup
def resolve_hostname(target):
    try:
        ip = socket.gethostbyname(target)
        print("[+] " + target + ": " + ip)
    except socket.error:
        print("[-] " + target + ": " + "Unable to resolve")
    except Exception as e:
        print("[-] " + target + ": " + "Unable to read input")

# Reverse lookup
def reverse_lookup(target):
    try:
        hostname = socket.gethostbyaddr(target)
        print("[+] " + str(target) + ": " + str(hostname[0]))
    except socket.error:
        print("[-] " + target + ": " + "Unable to resolve")
