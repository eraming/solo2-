
import glob
import os
import jinja2

all_html_files = glob.glob("./content/*.html")

pages = []

def compile_pages():
    for html_file in all_html_files:
        file_name = os.path.basename(html_file)
        # print(file_name)
        name_no_extension, extension = os.path.splitext(file_name)
        # print(name_no_extension)
        pages.append({
            'filename': ('./content/' + file_name),
            'output': ('./docs/' + file_name),
            'basename': file_name,
            'title': name_no_extension,
            'header': '{{ header }}',
        })


def open_base():
    base_template = open("./templates/base.html").read()
    return base_template

def open_content(page):
    content = open(page['filename']).read()
    return content

def compile(page, base_template, content):
    jinja_template = jinja2.Template(base_template)
    base_with_content = jinja_template.render(pages=pages, title=page['title'], content=content)
    return base_with_content

def write(page, base_with_content):
    final_page = open(page['output'], "w+").write(base_with_content)
    return final_page


def main():
    compile_pages()

    for page in pages:
        base_template = open_base()
        content = open_content(page)
        base_with_content = compile(page, base_template, content)
        write(page, base_with_content)





# print('------------- Example 3')

# template = Template('''
# Using if and for loops combined:
#
# {% for link in links %}
#     {% if link == selected_link %} >> {% endif %} {{ link }}
# {% endfor %}
# ''')
#
# list_of_links = [
#     'google.com',
#     'microsoft.com',
#     'facebook.com',
# ]
#
# selected = 'microsoft.com'
#
# results = template.render({
#     'links': list_of_links,
#     'selected_link': selected,
# })
# print(results)
