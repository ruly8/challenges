# Setup

The directory structure should look like this

```
├── admin-bot
│   ├── Dockerfile
│   ├── selenium-bot.py
│   ├── selenium-bot.py_BAK
│   └── templates
│       └── index.html
├── docker-compose.yml
├── README.md
└── target-site
    ├── app.py
    ├── Dockerfile
    └── templates
        ├── dashboard.html
        ├── home.html
        └── login.html
```

Change into the directory that contains the `docker-compose.yaml` and
run `docker-compose up`. Wait for both containers to finish loading and start exploring.

# Goal and Services

Goal is to leak the admin API key.

`http://localhost:5000` hosts the target site. You get the credentials
for a user account `user1:password1`.

`http://localhost:5001` hosts the admin bot which logs in as admin and clicks
the URL you provide.

# Disclaimer

Obviously given how the challenge is provided you have full access to all configs
and code and could just read the flag from `app.py` but that does not seem fun.
