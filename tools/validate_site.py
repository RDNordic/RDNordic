"""Offline checks for static page links, assets and bilingual site structure."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.refs, self.alternates = [], [], {}
        self.mains = self.h1s = 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.append(a['id'])
        self.mains += tag == 'main'
        self.h1s += tag == 'h1'
        for attr in ('href', 'src'):
            if attr in a:
                self.refs.append(a[attr])
        if tag == 'link' and a.get('rel') == 'alternate':
            self.alternates[a.get('hreflang')] = a.get('href')


def validate():
    pages = {p: Page(p.read_text(encoding='utf-8')) for p in ROOT.rglob('*.html')
             if not any(part.startswith('.') or part == 'node_modules'
                        for part in p.relative_to(ROOT).parts)}
    errors = []
    links = 0
    for path, page in pages.items():
        relative = path.relative_to(ROOT).as_posix()
        if len(set(page.ids)) != len(page.ids):
            errors.append(f'{relative}: duplicate IDs')
        if page.mains != 1 or page.h1s != 1:
            errors.append(f'{relative}: expected one main and one h1')
        if not {'en', 'no', 'x-default'} <= page.alternates.keys():
            errors.append(f'{relative}: missing language alternates')
        for ref in page.refs:
            url = urlsplit(urljoin('https://rdnordic.com/' + relative, ref))
            if url.scheme not in ('http', 'https') or url.netloc != 'rdnordic.com':
                continue
            links += 1
            target = ROOT / unquote(url.path).lstrip('/')
            if target.is_dir():
                target /= 'index.html'
            if not target.is_file():
                errors.append(f'{relative}: missing {ref}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{relative}: missing anchor {ref}')
    for error in errors:
        print(error)
    print(f'{len(pages)} pages, {links} local links/assets checked; {len(errors)} errors.')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(validate())
