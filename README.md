# SASEhack22F-NoBully

The ultimate anti-cyberbullying proxy application.
mitmproxy intercepts all web traffic and tracks bullying messages and reports to app.
Devpost: https://devpost.com/software/why-you-bully-me

## Setting up

### Backend
1. Cd to backend directory
2. Install dependencies with `pip install -r requirements.txt`
3. Run `python main.py`

### Frontend
1. Cd to frontend directory
2. Install dependencies with `npm install`
3. Run `npm start`

### Proxy Server
1. Install mitmproxy
2. Cd to `proxy`
3. Activate virtual environment `source venv/bin/activate`
4. Install requirements `pip install -r requirements.txt`
5. Run `main.py`
