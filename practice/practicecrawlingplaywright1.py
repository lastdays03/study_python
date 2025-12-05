from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # 브라우저 실행 (chromium, firefox, webkit 지원)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto('https://www.naver.com')
        
        # 클릭 및 입력
        # page.click('text=로그인')
        # page.fill('input[name="user"]', 'myuser')
        
        # 데이터 추출
        title = page.title()
        print(title)
        
        browser.close()

if __name__ == '__main__':
    run()