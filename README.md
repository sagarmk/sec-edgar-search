### SEC Edgar Panda

- Directly download with document type
- If you are just looking for few samples, restrict usage to first page download
#### Installation: 
    - python setup.py install
    
##### Notes:
    - have tested only with linux kernel
    - linux will require libnss3 

Quickstart:

```
from secpanda.extract import Extract

# sleep between extraction
sleep_time = 1

# default sleep time = 3
# default file limit = 10
downloader = Extract(sleep_time)
# printing extracted document links
print(downloader.search_and_extract('employment agreement'))

```

#### Extracting more than 10 samples
    
```
from secpanda.extract import Extract

limit = 100
sleep_time = 1

downloader = Extract(sleep_time)
downloader.search_keys('employment agreement')
downloader.extract_links(limit)
# printing extracted document links
print(downloader.get_list())
# close driver after extraction
downloader.exit_driver()

``` 


