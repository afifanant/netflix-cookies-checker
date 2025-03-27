from flask import Flask, request, render_template_string
import requests
from requests.cookies import RequestsCookieJar

app = Flask(__name__)

def parse_netscape_cookies(cookie_string):
    jar = RequestsCookieJar()
    cookies = cookie_string.split('\n')
    for cookie in cookies:
        cookie = cookie.strip()
        if not cookie or cookie.startswith('#'):
            continue
        try:
            parts = cookie.split('\t')
            if len(parts) >= 7:
                domain, flag, path, secure, expiration, name, value = parts
                jar.set(name, value, domain=domain, path=path, secure=(secure.lower() == 'true'))
        except ValueError:
            print(f"Warning: Invalid cookie format encountered: {cookie}")
    return jar

def validate_netflix_cookies(cookies):
    cookie_jar = parse_netscape_cookies(cookies)
    url = "https://www.netflix.com/browse"
    try:
        response = requests.get(url, cookies=cookie_jar, timeout=10)
        return response.status_code == 200 and "Your Account" in response.text
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist('file')
        results = []
        for file in files:
            if file:
                try:
                    cookies = file.read().decode('utf-8')
                except UnicodeDecodeError:
                    results.append(f"{file.filename}: Gagal membaca isi file")
                    continue

                is_valid = validate_netflix_cookies(cookies)
                result = f"{file.filename}: " + ("Sukses" if is_valid else "Gak Bisa Login")
                results.append(result)
        return render_template_string('''
            <!doctype html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
                <title>Netflix Cookies Checker</title>
                <style>
                    body { background-color: #f8f9fa; }
                    .container { max-width: 600px; margin-top: 50px; }
                    .header { text-align: center; margin-bottom: 30px; }
                    .header h1 { font-size: 2.5rem; font-weight: bold; }
                    .header p { color: #6c757d; font-style: italic; }
                    .content-box { background-color: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
                    .btn-primary, .btn-success { margin-top: 20px; }
                    .list-group-item { font-weight: bold; }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>Netflix Cookies Checker</h1>
                        <p>by Afif Ananta</p>
                    </div>
                    <div class="content-box">
                        <h2 class="mb-4">Hasil Validasi</h2>
                        <ul class="list-group">
                            {% for result in results %}
                                <li class="list-group-item">{{ result }}</li>
                            {% endfor %}
                        </ul>
                        <a href="/" class="btn btn-primary">Upload File Lagi</a>
                    </div>
                </div>
            </body>
            </html>
        ''', results=results)
    return '''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
        <title>Netflix Cookies Checker</title>
        <style>
            body { background-color: #f8f9fa; }
            .container { max-width: 600px; margin-top: 50px; }
            .header { text-align: center; margin-bottom: 30px; }
            .header h1 { font-size: 2.5rem; font-weight: bold; }
            .header p { color: #6c757d; font-style: italic; }
            .content-box { background-color: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
            .btn-success { margin-top: 20px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Netflix Cookies Checker</h1>
                <p>by Afif Ananta</p>
            </div>
            <div class="content-box">
                <h2 class="mb-4">Upload Cookies Files</h2>
                <form method="post" enctype="multipart/form-data">
                    <div class="form-group">
                        <label for="file">Pilih beberapa file cookies:</label>
                        <input type="file" name="file" id="file" multiple class="form-control-file">
                    </div>
                    <button type="submit" class="btn btn-success">Upload</button>
                </form>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
