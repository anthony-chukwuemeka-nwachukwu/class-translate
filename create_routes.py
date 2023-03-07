import os


def get_file_names(root_dir):
    file_names = []
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(subdir, file)
            file_names.append(file_path)
    return file_names

def handle_jinja2_error(html_file):
    with open(html_file) as f:
        lines=f.readlines()
    check_body = False
    with open(html_file,'w') as f:
        for line in lines:
            if '<body' in line:
                line = line.split('<body')
                f.write(line[0].replace('#','&#35;'))
                f.write('<body'+line[-1].replace('href="https://www.classcentral.com','href="').replace('pb.title','title'))
                check_body = True
            else:
                if check_body:
                    f.write(line.replace('href="https://www.classcentral.com','href="').replace('pb.title','title'))
                else:
                    f.write(line.replace('#','&#35;'))#.replace('https://www.classcentral.com','').replace('#','&#35;')

head = "from flask import Flask, render_template\napp = Flask(__name__)\n\n"
route_index = f"@app.route('/')\ndef index():\n\treturn render_template('index.html')\n\n"
route = lambda route_name, html, func: f"@app.route('{route_name}')\n@app.route('{route_name}/')\ndef {func}():\n\treturn render_template('{html}')\n"

file_path = 'src/templates'
raw_htmls = [f.replace('\\','/').split(file_path)[-1].strip() for f in get_file_names(file_path)]
htmls = [f.lstrip('/') for f in raw_htmls if f != '/index.html']

route_names = [f'/{f[:-5]}' if f.endswith('.html') else f.strip() for f in htmls]
funcs = [route_name.replace('/','_').replace('%20','_').replace('-','_').replace('=','_').strip().lstrip('_') for route_name in route_names]


with open('src/app.py','w') as f:
    f.write(head)
    f.write(route_index)
    for html,route_name,func in zip(htmls,route_names,funcs):
        f.write(route(route_name,html,func))
for raw_html in raw_htmls:
    handle_jinja2_error(f'{file_path}{raw_html}')