
import jinja2

pages = [
{
    "filename": "content/index.html",
    "output": "docs/index.html",
    "title": "home page",
    "header": "era ming",
},
{
    "filename": "content/gallery.html",
    "output": "docs/gallery.html",
    "title": "film photography",
    "header": "film photography",
},
{
    "filename": "content/projects.html",
    "output": "docs/projects.html",
    "title": "projects",
    "header": "past and current projects",
},
{
    "filename": "content/contact.html",
    "output": "docs/contact.html",
    "title": "Contact Me",
    "header": "how to reach me",
}
]


def compile(content, page):
    template = open("./templates/base.html").read()
    # finished_content = template.replace("{{content}}", content).replace("{{title}}", page['title']).replace("{{header}}", page['header'])
    jinja_template = jinja2.Template(template)
    finished_content = template.render(title=page['title'], content=content)
    return finished_content

def write(page, finished_content):
    final_page = open(page['output'], "w+").write(finished_content)
    return final_page

def main():
    for page in pages:
        print(page['filename']) #to see if the function gives an output
        content = open(page['filename']).read()
        #now invoking functions compile() and write()
        full_compile = compile(content, page)
        write(page, full_compile)

if __name__ == "__main__":

    main()
