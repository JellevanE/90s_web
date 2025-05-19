# 90s Web

This repository contains a small retro 1990s style website. Each page is written in plain HTML and styled with `90s_style.css`.

## Testing Locally

Open `index.html` directly in your browser or run a simple HTTP server from the repository directory:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000` to browse the site.

## Hosting

Any static website host can serve this project.

### GitHub Pages
1. Push the repository to GitHub.
2. Enable GitHub Pages in the repository settings, choosing the `main` branch and `/` root.
3. Your pages will be available at `https://<username>.github.io/<repository>`.

### Custom Domain
1. Upload these files to any hosting provider that supports static sites (or to your own server).
2. Register a domain name with a registrar if you haven't already.
3. Update your domain's DNS records (typically an A or CNAME record) to point to your host.
4. After DNS propagation, visit your domain to see the site live.

