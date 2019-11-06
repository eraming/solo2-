#go into the docs/ directory

import os
os.chdir('docs/')

#index page ----------->

index_top = open('../templates/top.html').read()
index_content = open('../content/index.html').read()
index_bottom = open('../templates/bottom.html').read()
index = index_top + index_content + index_bottom
open("index.html", "w+").write(index)

#gallery page --------->

gallery_top = open('../templates/top.html').read()
gallery_content = open('../content/gallery.html').read()
gallery_bottom = open('../templates/bottom.html').read()
gallery = gallery_top + gallery_content + gallery_bottom
open("gallery.html", "w+").write(gallery)

#project page --------->

projects_top = open('../templates/top.html').read()
projects_content = open('../content/projects.html').read()
projects_bottom = open('../templates/bottom.html').read()
projects = projects_top + projects_content + projects_bottom
open("projects.html", "w+").write(projects)

#contact page --------->

contact_top = open('../templates/top.html').read()
contact_content = open('../content/contact.html').read()
contact_bottom = open('../templates/bottom.html').read()
contact = contact_top + contact_content + contact_bottom
open("contact.html", "w+").write(contact)
