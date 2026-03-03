# intelligence/waf_detector.py
def detect_waf(engine, url):
    try:
        r = engine.get(url)
        headers = str(r.headers).lower()
        if "cloudflare" in headers: return "Cloudflare"
        if "sucuri" in headers: return "Sucuri"
        if "akamai" in headers: return "Akamai"
        if "incapsula" in headers: return "Imperva Incapsula"
    except: pass
    return "No WAF Detected"
