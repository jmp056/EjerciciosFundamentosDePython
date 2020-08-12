from urllib.parse import urlparse

def obtener_hostname(url):
    hostname = urlparse(url)
    print(hostname.netloc)

obtener_hostname("https://uasdvirtual.uasd.eud.do/diplomados/my")
obtener_hostname("https://github.com/cjgarcia/diplomado_python")