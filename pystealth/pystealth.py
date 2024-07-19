import asyncio

class PyStealth:
    @staticmethod
    async def _prevent_stack_access(page):
        script = '''
        () => {
            const originalError = Error;
            function CustomError(...args) {
                const error = new originalError(...args);
                Object.defineProperty(error, 'stack', {
                    get: () => '',
                    configurable: false
                });
                return error;
            }
            CustomError.prototype = originalError.prototype;
            window.Error = CustomError;

            const observer = new MutationObserver(() => {
                if (window.Error !== CustomError) {
                    window.Error = CustomError;
                }
            });
            observer.observe(document, { childList: true, subtree: true });
        }
        '''
        await page.evaluate(script)

    @classmethod
    def _get_script(cls):
        return '''
        (() => {
            const originalError = Error;
            function CustomError(...args) {
                const error = new originalError(...args);
                Object.defineProperty(error, 'stack', {
                    get: () => '',
                    configurable: false
                });
                return error;
            }
            CustomError.prototype = originalError.prototype;
            window.Error = CustomError;

            const observer = new MutationObserver(() => {
                if (window.Error !== CustomError) {
                    window.Error = CustomError;
                }
            });
            observer.observe(document, { childList: true, subtree: true });
        })();
        '''

    @classmethod
    async def setup_pyppeteer(cls, page):
        await page.evaluateOnNewDocument(f'() => {{ {cls._get_script()} }}')
        page.on('load', lambda: asyncio.ensure_future(cls._prevent_stack_access(page)))

    @classmethod
    async def setup_playwright(cls, page):
        await page.evaluate(cls._get_script())
        page.on('load', lambda: asyncio.ensure_future(cls._prevent_stack_access(page)))

    @classmethod
    def setup_selenium(cls, driver):
        script = f'''
        (() => {{
            const originalDocumentWrite = document.write;
            document.write = function(...args) {{
                if (!document.body) {{
                    const div = document.createElement('div');
                    div.innerHTML = args.join('');
                    document.documentElement.appendChild(div);
                }} else {{
                    originalDocumentWrite.apply(this, args);
                }}
            }};

            function runScript() {{
                {cls._get_script()}
            }}

            if (document.readyState === 'loading') {{
                document.addEventListener('DOMContentLoaded', runScript);
            }} else {{
                runScript();
            }}
        }})();
        '''
        driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': script})