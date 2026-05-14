
#!/usr/bin/env python3

import requests
import argparse
import sys
import time

VERSION = "2.0"


def banner():
    title = r'''
██████╗ ██╗██████╗ ██╗   ██╗ █████╗ ███╗   ██╗ █████╗
██╔══██╗██║██╔══██╗██║   ██║██╔══██╗████╗  ██║██╔══██╗
██║  ██║██║██████╔╝██║   ██║███████║██╔██╗ ██║███████║
██║  ██║██║██╔══██╗╚██╗ ██╔╝██╔══██║██║╚██╗██║██╔══██║
██████╔╝██║██║  ██║ ╚████╔╝ ██║  ██║██║ ╚████║██║  ██║
╚═════╝ ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
    '''

    print("\033[91m" + title + "\033[0m")
    print("\033[96m" + "        Dirvana | Made by Arghya Sikdar ©" + "\033[0m")
    print()


def dir_traversal_scan(url, wordlist_file):
    try:
        with open(wordlist_file, "r") as file:
            directory_traversals = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("\033[91m[!] Wordlist file not found.\033[0m")
        sys.exit(1)

    print(f"\033[93m[~] Starting scan on {url} with {len(directory_traversals)} entries...\033[0m\n")
    time.sleep(1)

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for traversal in directory_traversals:
        full_url = f"{url.rstrip('/')}/{traversal.lstrip('/')}"

        try:
            response = requests.get(
                full_url,
                headers=headers,
                timeout=5,
                allow_redirects=True
            )

            if response.status_code == 200:
                if "Index of" in response.text or "Parent Directory" in response.text:
                    print(f"\033[92m[{response.status_code}] {full_url} - Directory Found\033[0m")
                else:
                    print(f"\033[94m[{response.status_code}] {full_url} - Page Found\033[0m")

            elif response.status_code == 301 or response.status_code == 302:
                print(f"\033[96m[{response.status_code}] {full_url} - Redirected\033[0m")

            elif response.status_code == 403:
                print(f"\033[95m[{response.status_code}] {full_url} - Forbidden\033[0m")

            elif response.status_code == 404:
                print(f"[{response.status_code}] {full_url} - Not Found")

            else:
                print(f"[{response.status_code}] {full_url}")

        except requests.Timeout:
            print(f"\033[91m[!] Timeout while connecting to {full_url}\033[0m")

        except requests.RequestException as e:
            print(f"\033[91m[!] Error connecting to {full_url}: {e}\033[0m")


def main():
    parser = argparse.ArgumentParser(
        description="Directory Traversal Scanner - Dirvana"
    )

    parser.add_argument(
        "-u",
        "--url",
        required=False,
        help="Target URL"
    )

    parser.add_argument(
        "-w",
        "--wordlist",
        required=False,
        help="Wordlist file"
    )

    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Show version info and exit"
    )

    if len(sys.argv) == 1:
        banner()
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    if args.version:
        banner()
        print(f"\033[93mDirvana v{VERSION} by Arghya Sikdar\033[0m")
        sys.exit(0)

    if not args.url or not args.wordlist:
        banner()
        parser.print_help(sys.stderr)
        sys.exit(1)

    banner()
    dir_traversal_scan(args.url, args.wordlist)


if __name__ == "__main__":
    main()