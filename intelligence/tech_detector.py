# intelligence/tech_detector.py
def detect_technology(engine, url):
    try:
        r = engine.get(url)
        server = r.headers.get("Server", "Unknown")
        powered = r.headers.get("X-Powered-By", "Unknown")
        return server, powered
    except:
        return "Unknown", "Unknown"
