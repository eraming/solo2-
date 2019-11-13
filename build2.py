

pages = [
{
    "filename": "content/index.html",
    "output": "docs/index.html",
    "title": "Home Page",
},
{
    "filename": "content/gallery.html",
    "output": "docs/gallery.html",
    "title": "Film Photography",
},
{
    "filename": "content/projects.html",
    "output": "docs/projects.html",
    "title": "Projects",
},
{
    "filename": "content/contact.html",
    "output": "docs/contact.html",
    "title": "Contact Me",
}
]

def compile(content, page):
    template = open("./templates/base.html").read()
    finished_content = template.replace("{{content}}", content).replace("{{title}}", page['title'])
    # returning the string replacement for content and title
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
