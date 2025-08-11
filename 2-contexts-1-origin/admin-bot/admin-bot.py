from flask import Flask, render_template, request, redirect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import threading

app = Flask(__name__)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

def run_selenium(url_to_open):
    driver = webdriver.Chrome(options=options)

    try:
        driver.get('http://localhost:5000/login')

        time.sleep(2)

        username_field = driver.find_element(By.NAME, 'username')
        password_field = driver.find_element(By.NAME, 'password')

        username_field.send_keys('admin')
        password_field.send_keys('sup3r-s3cr3t-4dm1n-p4s5w0rd')

        password_field.send_keys(Keys.RETURN)

        time.sleep(2)

        if "Welcome" in driver.page_source:
            print("Login successful!")

            driver.get(url_to_open)

            time.sleep(2)

            print(f"Successfully opened the URL: {driver.current_url}")
        else:
            print("Login failed.")

    finally:
        driver.quit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        threading.Thread(target=run_selenium, args=(url,)).start()
        return redirect('/')

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
