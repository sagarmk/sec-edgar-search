### SEC Edgar Panda

- Directly download with document type
- Sec allows us to download documents till a maximum of 10 pages
- If you are just looking for few samples, restrict usage to first page download
####Installation: 
    - python setup.py install
    ##### Notes:
        - have tested only with linux kernel
        - linux will require libnss3 

Quickstart:

    ```
    from secpanda.extract import Extract
    downloader = Extract()
    downloader.search_keys("Employment Agreement")
    links = downloader.extract_links()
    # wget on links to download them

    ``` 


