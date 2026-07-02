import requests


def main():
    print("Hello from sbom-slsa-attestations-example!")

    r = requests.get("https://www.google.com")
    if r.status_code == 200:
        print("What did you expect ?")
    else:
        print("Something's gone terribly wrong !")


if __name__ == "__main__":
    main()
