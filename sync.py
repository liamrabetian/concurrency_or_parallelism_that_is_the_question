import time
import requests


def download_site(url, session):
    with session.get(url) as response:
        print(f'read {len(response.content)} from {url}')


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == '__main__':
    sites = [
        'https://www.jython.org',
        'https://www.python.org',
    ] * 80

    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f'Downloaded {len(sites)} in {duration} seconds!')
