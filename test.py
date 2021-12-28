from src.secpanda.extract import Extract

if __name__ == "__main__":

    emp = Extract()
    emp.search_keys('employment agreement')
    links_to_download = emp.extract_links()
    print("List of urls downloaded :: ",links_to_download)