# Scrapy settings for ifttt project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

# BOT_NAME = 'ifttt'
# 
SPIDER_MODULES = ['ewescrapers.spiders']
NEWSPIDER_MODULE = 'ewescrapers.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'ewescrapers (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
     'ewescrapers.pipelines.RemoveEmptyItemsPipeline' : 900,
#     # 'ewescrapers.pipelines.LogPipeline',
#     # 'ewescrapers.pipelines.FileExporterPipeline',
#     'ewescrapers.pipelines.IdRegistryPipeline' : 100
      'ewescrapers.pipelines.PopulateParameterIds' : 700
    }

FEED_EXPORTERS = {
    # 'rdf' : 'ewescrapers.rdf.jinja_exporters.JinjaExporter',
    'rdf' : 'ewescrapers.rdf.jinja_exporters.JinjaExporterMultifile',
    # 'rdf2' : 'ewescrapers.rdf.exporter.RdfExporter',
    'json': 'scrapy.exporters.JsonItemExporter',
    'jsonlines': 'scrapy.exporters.JsonLinesItemExporter',
    'csv': 'scrapy.exporters.CsvItemExporter',
    'xml': 'scrapy.exporters.XmlItemExporter',
}