from mechanize import Browser
br = Browser()
br.open("http://www.avenida21.es/")
print br.title()
