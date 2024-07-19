# PyStealth 🕵️‍♂️

PyStealth is a powerful Python module designed to enhance the stealth capabilities of your web automation projects. It works seamlessly with popular frameworks like Selenium, Puppeteer, and Playwright to prevent detection of CDP.

### 🛡️ Key Features

- 🔒 Prevents stack trace access, making it harder to detect automation
- 🌐 Compatible with Selenium, Puppeteer, and Playwright
- 🎭 Enhances the stealth of your web scraping and testing projects
- 🔧 Easy to integrate with existing code

## 🔧 Installation

Install PyStealth easily with pip:

```bash
pip install pystealth
```

## 🚀 Quick Start

Here's how to use PyStealth with different frameworks:

### Selenium

```python
from selenium import webdriver
from pystealth import PyStealth

driver = webdriver.Chrome()
PyStealth.setup_selenium(driver)
```

### Pyppeteer

```python
import asyncio
from pyppeteer import launch
from pystealth import PyStealth

async def main():
    browser = await launch()
    page = await browser.newPage()
    await PyStealth.setup_pyppeteer(page)
    
asyncio.get_event_loop().run_until_complete(main())
```

### Playwright

```python
from playwright.async_api import async_playwright
from pystealth import PyStealth

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await PyStealth.setup_playwright(page)

asyncio.run(main())
```

### Playwright over CDP

```python
import asyncio
from playwright.async_api import async_playwright
from pystealth import PyStealth

async def main():
    port = 9222  # Replace with your CDP port
    ws_endpoint = "/devtools/browser/..."  # Replace with your WebSocket endpoint

    async with async_playwright().start():
        browser = await p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_endpoint}')
        context = browser.contexts[0]
        page = context.pages[0]

        await PyStealth.setup_playwright(page)

        # Your automation code here

        await browser.close()

asyncio.run(main())
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/DedInc/pystealth/issues).

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.