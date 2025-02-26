from safarnama import load_config, SiteCrawler

# # Crawl python.org
# config_python = load_config("config_python.yaml")
# crawler_python = SiteCrawler(config_python)
# visited_python = crawler_python.crawl()
# print(f"Crawled {len(visited_python)} URLs from python.org.")

# # Optionally, generate a sitemap for python.org
# sitemap_python = crawler_python.generate_sitemap(visited_python)
# sitemap_python.write("data/sitemap_python.xml", encoding="utf-8", xml_declaration=True)
# crawler_python.close()

# Crawl wiki.python.org
config_wiki = load_config("config_wiki.yaml")
crawler_wiki = SiteCrawler(config_wiki)
visited_wiki = crawler_wiki.crawl()
print(f"Crawled {len(visited_wiki)} URLs from wiki.python.org.")

# Optionally, generate a sitemap for wiki.python.org
sitemap_wiki = crawler_wiki.generate_sitemap(visited_wiki)
sitemap_wiki.write("data/sitemap_wiki.xml", encoding="utf-8", xml_declaration=True)
crawler_wiki.close()
