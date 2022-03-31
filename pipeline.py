import functionalities
from pipeline_getter import get_pipeline_config
from driver import get_driver



def pipeline_runner(scraper):
    config = get_pipeline_config(scraper)
    print(f"Running Pipeline for connector \"{config.name}\"")
    driver = get_driver()
    html_pages = []
    for function in config.functions:
        params = function.get("params", {})
        f = getattr(functionalities, function.name)
        html_page = f(driver, **params)
        html_pages.append(html_page)
    return html_pages