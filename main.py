# from rich import print as rprint

# rprint('[black on red]Hello[/] [black on green]World[/]')

# Contains divs with data
# /html/body/div/div/div/div[2]/div/div/div/div/div/div/div[3]/div[4]/div[1]/div/div/div[1]/div/div/div/div[2]

# Class name for line numbers
# diff-row-content_diffLineNumber__OqSwI

# Divs with content x2 (before and after)
# Contains span for content
#   Value of each word + their color if any must be added and appended!

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from rich import print as rprint

URL = 'https://www.diffchecker.com/24WUfeQl/'

def main():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    op.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=op)
    rprint('[yellow]Fetching URL[/yellow]')
    driver.get(URL)
    rprint('[green]Success[/green]')
    
    try:
        rprint('[yellow]Fetching Container Div[/yellow]')
        container_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/div/div/div/div[3]/div[4]/div[1]/div/div/div[1]/div/div/div/div[2]')))
        rprint('[green]Success[/green]')
        rprint('[yellow]Fetching Row Divs[/yellow]')
        row_divs = container_div.find_elements(By.XPATH, './div')
        rprint(f'[pink]no. of row_divs: {len(row_divs)}[/pink]')
        for rd in row_divs:
            placeholder_divs = rd.find_elements(By.XPATH, './div')
            arrow_applied = False
            for pd in placeholder_divs:
                # rprint(f'[purple]no. of placeholder_divs: {len(placeholder_divs)}[/purple]')
                if pd.get_attribute('class') != 'diff-row-content_diffLineNumber__OqSwI':
                    data_spans = pd.find_elements(By.XPATH, './span')
                    # rprint(f'[blue]no. of data_spans: {len(data_spans)}[/blue]')
                    for ds in data_spans:
                        text = ds.text
                        color_class = ds.get_attribute('class')
                        color = 'transparent'
                        
                        if 'diff-chunk_diffChunkRemoved__iwVpA' in color_class:
                            color = 'red'
                        elif 'diff-chunk_diffChunkInserted__DlyJg' in color_class:
                            color = 'green'
                            
                        if color != 'transparent':
                            rprint(f'[black on {color}]{text}[/]', end='')
                        else:
                            rprint(text, end='')
                    if not arrow_applied:
                            rprint(' -> ', end='')
                            arrow_applied = True
            rprint()
        pass
    except Exception as e:
        print(e)
        driver.quit()
    
    driver.quit()
    
if __name__ == '__main__':
    main()
    
