import asyncio, pathlib
from playwright.async_api import async_playwright

IDS = ["hero", "notchestra", "bioamazon", "sampaio", "vagas"]
here = pathlib.Path(__file__).parent

(here / "out").mkdir(exist_ok=True)

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 960, "height": 2400}, device_scale_factor=2)
        await pg.goto((here / "pieces.html").as_uri())
        await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(400)
        for i in IDS:
            await pg.locator(f"#{i}").screenshot(path=str(here / "out" / f"{i}.png"), omit_background=True)
        await b.close()

asyncio.run(main())
