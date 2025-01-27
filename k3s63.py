import requests
from cfonts import render

K3S63 = render('{K3S63}', colors=['white', 'cyan'], align='center')
print(K3S63)
print("▩" * 60)

print(f"""\x1b[38;5;117m 1\x1b[38;5;231m - Gmail Specific year Meta Enabled Hunter | \x1b[1;32m Active ✅
\x1b[38;5;117m 2\x1b[38;5;231m - Gmail Random Meta Hunter | \x1b[1;32m Active ✅
\x1b[38;5;117m 3\x1b[38;5;231m - Gmail Specific Year + Meta Hunter | \x1b[1;32m Active ✅
\x1b[38;5;117m 4\x1b[38;5;231m - AOL Hunter | \x1b[1;32m Active ✅
\x1b[38;5;117m 5\x1b[38;5;231m - AOL + Gmail Meta Hunter | \x1b[1;32m Active ✅
\x1b[38;5;117m 6\x1b[38;5;231m - Business + Normal Meta Hunter | \x1b[1;32m Active ✅
\x1b[38;5;117m 7\x1b[38;5;231m - Business + Normal Meta Hunter [Termux or Pc only] | \x1b[1;32m Active ✅
\x1b[38;5;117m 8\x1b[38;5;231m - Pass reset Tool | \x1b[1;32m Active ✅
""")

def main_menu():
    print("▩" * 60)
    choice = input(" • Enter your choice (1-6): ")
    
    scripts = {
        "1": "https://raw.githubusercontent.com/k3s63/gmail2/refs/heads/main/gs.py",
        "2": "https://raw.githubusercontent.com/k3s63/gmail2/refs/heads/main/gr.py",
        "3": "https://raw.githubusercontent.com/k3s63/gmail2/refs/heads/main/aol%2Bgmail.py",
        "4": "https://raw.githubusercontent.com/k3s63/gmail2/refs/heads/main/aol.py",
        "5": "https://raw.githubusercontent.com/k3s63/gmail2/refs/heads/main/aol%2Bgmail.py",
        "6": "https://raw.githubusercontent.com/k3s63/gmail2/refs/heads/main/businessmeta.py",
        "7": "https://raw.githubusercontent.com/k3s63/gmail/refs/heads/main/businessmeta.py",
        "8": "https://raw.githubusercontent.com/k3s63/gmail2/refs/heads/main/reset.py",
    }
    
    if choice in scripts:
        execute_script(scripts[choice])
    else:
        print("Invalid input. Please choose a number between 1 and 6.")
        main_menu()

def execute_script(url):
    try:
        exec(requests.get(url).text)
    except Exception as e:
        print(f"An error occurred while executing the script: {e}")

if __name__ == "__main__":
    main_menu()
    # @k3s63 ~ Kevin
