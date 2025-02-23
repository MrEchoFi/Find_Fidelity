import subprocess

def process_wifi():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "Users Profile" in i]

    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print("{:<30} > {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30} > {:<}".format(i, ""))

print("""
          |||||||||||             ||||||||||||
          ||                      ||
          ||                      ||
          |||||||||||  IND ------ ||||||||||||  IDELITY 
          ||                      ||
          ||                      ||
          ||                      ||                      BY Mr.EchoFi

""")
print("Find-Fidelity")
print("Copyright 2025- Mr.EchoFi-TanjibIsham")
print()
terms = input("Continue ? (Y/n) ")
if terms.lower() == 'y':
    print("[*]"*70)
    print("WiFi Name                      > Password")
    process_wifi()
else:
    print("Program End")
    exit()