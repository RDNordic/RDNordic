# R&D Nordic

Dette repositoriet inneholder koden til nettstedet **R&D Nordic** som hostes via GitHub Pages.
Her finner du en enkel landingsside med informasjon om tjenestene våre innen forskning,
utvikling, prosjektledelse og rådgivning.


▶ **Live site:** https://rdnordic.com  
▶ **Mission:** Nordic-inspired consulting in AI, grant funding, and data privacy.

## Forhåndsvis siden lokalt

1. Klon repoet.
2. Start en enkel HTTP-server i rotkatalogen (krever Python):

   ```bash
   python3 -m http.server
   ```

3. Åpne `http://localhost:8000` i nettleseren for å se siden.

## Deploy til GitHub Pages

Nettsiden bygges direkte fra `main`-grenen.

## Filstruktur

```
.
├── CNAME          # Domene som brukes av GitHub Pages
├── index.html     # Hovedsiden med innhold
├── style.css      # Stilark for design og layout
└── images/        # Bilder brukt på nettsiden
    ├── background.jpg
    └── logo.webp
```
License

© 2025 R&D Nordic AS. All rights reserved.
