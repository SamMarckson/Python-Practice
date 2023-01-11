"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""

def domain_name(url):
    nomeUrl = []

    if 'www.' in url:                    #PRIMEIRO CASO
        for i in range(4, len(url)):
            if url[i-4] == 'w' and url[i-3] == 'w' and url[i-2] == 'w' and url[i-1] == '.':
                while url[i] != '.' and i < len(url):
                    nomeUrl.append(url[i])
                    i += 1
                return ''.join(nomeUrl)


    if '//' not in url and 'www.' not in url:       #SEGUNDO CASO
        for i in range(0, len(url)):
            while url[i] != '.' and i < len(url):
                nomeUrl.append(url[i])
                i += 1
            return ''.join(nomeUrl)

    for i in range(1, len(url)):         #TERCEIRO CASO
        if url[i-1] == '/' and url[i] != '/':
            while url[i] != '.' and i < len(url):
                nomeUrl.append(url[i])
                i += 1
            return ''.join(nomeUrl)


    for i in range(1, len(url)):   #QUARTO CASO
        if url[i - 1] == '.':
            while url[i] != '.' and i < len(url):
                nomeUrl.append(url[i])
                i += 1
            return ''.join(nomeUrl)


#MAIN
print(domain_name("http://google.com"))



