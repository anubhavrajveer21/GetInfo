import webbrowser

class Link:
    TRUSTED_TOP_LEVEL_DOMAINS = ('com', 'gov', 'in', 'edu', 'net', 'org')
    TRUSTED_INTERNET_PROTOCOL = "https"

    def __init__(self, link: str):
        self.link = link
        self.internet_protocol = ""
        self.top_level_domain = ""
        self.domain = ""
        self.sub_domains = []
        self.hostname = ""
        self.route = ""
        self.has_sub_domain = None

        for char in link:
            if char == ':':
                link = link.replace(f'{self.internet_protocol}://', '')
                break
            self.internet_protocol += char
        else:
            raise ValueError(f"'{link}' is not a valid link!")
        
        for char in link:
            if char == "/":
                self.route = link[link.find(char):].replace('/', '')
                link = link.replace(f"/{self.route}", '')
                self.hostname = link
                break
        
        splitted_domains = link.split('.')
        if len(splitted_domains) < 2:
            raise ValueError(f"'{link}' is not a valid link!")

        self.has_sub_domain = splitted_domains[-2:] != splitted_domains
        self.domain = splitted_domains[-2:][0]
        self.top_level_domain = splitted_domains[-2:][1]
        splitted_domains.remove(splitted_domains[-2:][0])
        splitted_domains.remove(splitted_domains[-2:][1])

        self.sub_domains = splitted_domains


    def __str__(self) -> str:
        return self.link


    def is_safe(self) -> bool:
        protocol_is_trusted = Link.TRUSTED_INTERNET_PROTOCOL == self.internet_protocol
        top_level_domain_is_trusted = self.top_level_domain in Link.TRUSTED_TOP_LEVEL_DOMAINS

        return protocol_is_trusted and top_level_domain_is_trusted


    def open(self) -> None:
        webbrowser.open_new_tab(self.link)
