import importlib.metadata

import requests


def main():
    version = importlib.metadata.version("sbom-slsa-attestations-example")
    print(f"Hello from sbom-slsa-attestations-example version {version} !")

    r = requests.get("https://www.google.com")
    if r.status_code == 200:
        print("What did you expect ?")
    else:
        print("Something's gone terribly wrong, most probably your DNS..")


if __name__ == "__main__":
    main()
