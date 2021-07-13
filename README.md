# Drifter Food Template

This template is a simple scrapy projet which is designed to unify and automate some parts od scraping process.

Template includes:
- import XPaths and Data format
- input/output filenaming
- the same file format (csv)
- the same encoding (utf-8-sig)
- random User Agent
- IP Proxy


# Requirements

scrapy-random-useragent

# Usage

- add website information to the file config_import.json
- create your own files in spiders directory, remember these files are the only free workspaces for you :)

In spiders directory you can find examples of spider and scraper scripts.

The spider and scraper output files you can find in one of this folders:
- 1-target-urls - spider final output file (without duplicates)
- 2-raw-data - scraper final output file
- 3-clean-data - spider initial output file (with duplicates)


# Warning

- Don't change anything in settings.py! If you want to add additional settings, use custom_settings, but first add them to the file config_import.json (scraping_rules), see example Download delay

# Deployment

- To run it use the default scrapy way: `scrapy crawl example_scraper`

- Please run this at the same level as `scrapy.cfg` file.
