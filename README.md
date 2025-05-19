# 90s Web

This repository contains a small retro 1990s style website. Each page is written in plain HTML and styled with `90s_style.css`.

## Testing Locally

Open `index.html` directly in your browser or run a simple HTTP server from the repository directory:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000` to browse the site.

### Running the chat server

The chatbot needs a small Python backend. Install the requirements and start the server:

```bash
pip install -r requirements.txt
python3 chat_server.py
```

Once the server is running, open the site in another tab at `http://localhost:5000` to test the chat page.

### Chat data flow

`chat.html` uses JavaScript to send a `POST` request to `/api/chat` whenever a user submits a message. The JSON payload contains the current message and the conversation history. `chat_server.py` receives this data, processes it (currently with a dummy reply), and returns a JSON object with the bot's response and updated history. The browser script appends the response to the chat box so the conversation continues in the page.

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

You can also host the files with other services that support static sites.

