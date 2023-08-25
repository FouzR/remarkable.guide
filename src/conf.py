import time
from datetime import datetime

year = datetime.today().year

project = "reMarkable Guide"
copyright = f"2023-{year}, Eeems"
author = "Nathaniel 'Eeems' van Diepen"

html_theme_path = ["_themes"]
html_static_path = ["_static"]
templates_path = ["_templates"]

highlight_language = "shell"
html_title = "reMarkable Guide"
html_theme = "oxide"
master_doc = "sitemap"
html_sidebars = {"**": ["nav.html", "sidefooter.html"]}
html_permalinks_icon = "#"
html_baseurl = "https://remarkable.guide"
html_use_opensearch = "https://remarkable.guide"
html_js_files = [
    f"oxide.js?_t={time.time()}",
    "https://peek.eeems.website/peek.js",
    (
        "https://browser.sentry-cdn.com/6.16.1/bundle.tracing.min.js",
        {
            "integrity": "sha384-hySah00SvKME+98UjlzyfP852AXjPPTh2vgJu26gFcwTlZ02/zm82SINaKTKwIX2",
            "crossorigin": "anonymous",
        },
    ),
    (
        "https://giscus.app/client.js",
        {
            "data-repo": "Eeems-Org/remarkable.guide",
            "data-repo-id": "R_kgDOI7Ab8A",
            "data-category": "General",
            "data-category-id": "DIC_kwDOI7Ab8M4CY3cm",
            "data-mapping": "pathname",
            "data-strict": "1",
            "data-reactions-enabled": "1",
            "data-emit-metadata": "1",
            "data-input-position": "top",
            "data-theme": "transparent_dark",
            "data-lang": "en",
            "data-loading": "lazy",
            "crossorigin": "anonymous",
            "async": "async",
        },
    ),
]

# Do not enable sphinx.ext.autosectionlabel
# The expectation is that we explicitely add references
extensions = [
    "sphinxcontrib.fulltoc",
    "breathe",
]
