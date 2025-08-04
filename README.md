# Luna LAN Blackboard

A simple, password-protected notes app for sharing text in your local network (LAN).
No cloud. No accounts. Crew-only.

---

## 🚀 Features

* Web-based: Edit notes from any device on your LAN
* Autosave ("bounce"): Updates 3 seconds after typing/copy
* Manual save and auto-refresh
* Password protected
* Secret/password never hardcoded (file or env variable)
* No database needed — just RAM
* Built with Flask and by custom AI

---

## 📦 Install

1. **Clone this repo (or copy files):**

   ```bash
   git clone https://github.com/yourcrew/luna_lan_blackboard.git
   cd luna_lan_blackboard
   ```

2. **(Recommended) Use ********************[pipx](https://pypa.github.io/pipx/)********************, ********************[pip](https://pip.pypa.io/)********************, or PyPy:**

   **With pip:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install flask
   ```

   **Or with ********************[pipx](https://pypa.github.io/pipx/)********************:**

   ```bash
   pipx run flask
   ```

   **Or with PyPy (faster Python):**

   ```bash
   # Install pypy (see https://www.pypy.org/)
   pypy3 -m venv venv
   source venv/bin/activate
   pip install flask
   ```

3. **Create a password file (recommended):**

   ```bash
   echo "your_crew_password" > ~/.blackboard_pw
   chmod 600 ~/.blackboard_pw
   ```

   *Or set an environment variable:*

   ```bash
   export LUNA_BLACKBOARD_PASS="your_crew_password"
   ```

4. **(Optional but recommended) Set a long, random secret for Flask sessions:**

   ```bash
   export LUNA_BLACKBOARD_SECRET="random_long_string_change_this"
   ```

---

## 🏁 Run

```bash
python3 luna_lan_blackboard_pw.py
# or with PyPy:
pypy3 luna_lan_blackboard_pw.py

```

Open your browser to:
**http\://\[your-pc-ip]:5137**

Login with your password.

---

## 🛡️ Security

* Password never in code: keep in `~/.blackboard_pw` or env var
* Local LAN only! Don’t expose to WAN without HTTPS & extra security

---

## 📝 Customize

* All HTML templates in `/templates/`
* Change port or add more features as you wish
