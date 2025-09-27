from pathlib import Path
from yaml import safe_load

DATA_DIR = Path("docs") / "data"

def _read_yaml(name):
    path = (DATA_DIR / name).resolve()
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        data = safe_load(f) or []
    return data

def define_env(env):
    @env.macro
    def load_yaml(name):
        return _read_yaml(name)

    @env.macro
    def team_cards(yaml_file="team.yml"):
        people = _read_yaml(yaml_file)
        out = []
        out.append('<div class="po-grid">')
        for p in people:
            name = p.get("name","")
            role = p.get("role","")
            handle = p.get("handle","")
            portrait = p.get("portrait","assets/placeholder-portrait.svg")
            links = p.get("links", {})
            link_html = ""
            if isinstance(links, dict):
                items = []
                for k, v in links.items():
                    items.append(f'<a href="{v}" target="_blank" rel="noopener">{k}</a>')
                if items:
                    link_html = '<div class="po-links">' + " · ".join(items) + "</div>"
            out.append(f'''
            <article class="po-card">
              <div class="po-card-media">
                <img alt="{name}" src="{portrait}" loading="lazy">
              </div>
              <div class="po-card-body">
                <h3>{name}</h3>
                <div class="po-meta">{role}</div>
                <div class="po-handle">{handle}</div>
                {link_html}
              </div>
            </article>
            ''')
        out.append('</div>')
        return "\n".join(out)

    @env.macro
    def character_cards(yaml_file="characters.yml"):
        chars = _read_yaml(yaml_file)
        out = []
        out.append('<div id="po-char-grid" class="po-grid">')
        for c in chars:
            name = c.get("name","")
            callsign = c.get("callsign","")
            role = c.get("role","")
            faction = c.get("faction","")
            clearance = c.get("clearance","")
            status = c.get("status","Active")
            bio = c.get("bio","")
            portrait = c.get("portrait","assets/placeholder-portrait.svg")
            idx = f"{name} {callsign} {role} {faction} {clearance} {status}".lower()
            out.append(f'''
            <article class="po-card" data-index="{idx}">
              <div class="po-card-media">
                <img alt="{name}" src="{portrait}" loading="lazy">
              </div>
              <div class="po-card-body">
                <h3>{name}</h3>
                <div class="po-meta">{role} · {faction}</div>
                <div class="po-badges">
                  <span class="po-badge">Callsign: {callsign}</span>
                  <span class="po-badge">Clearance: {clearance}</span>
                  <span class="po-badge status-{status.lower()}">{status}</span>
                </div>
                <p class="po-bio">{bio}</p>
              </div>
            </article>
            ''')
        out.append('</div>')
        return "\n".join(out)

    @env.macro
    def map_tiles(yaml_file="maps.yml"):
        maps = _read_yaml(yaml_file)
        out = []
        out.append('<div class="po-grid">')
        for m in maps:
            name = m.get("name","")
            zone = m.get("zone","")
            summary = m.get("summary","")
            image = m.get("image","assets/placeholder-map.svg")
            out.append(f'''
            <article class="po-card">
              <div class="po-card-media wide">
                <img alt="{name}" src="{image}" loading="lazy">
              </div>
              <div class="po-card-body">
                <h3>{name}</h3>
                <div class="po-meta">{zone}</div>
                <p>{summary}</p>
              </div>
            </article>
            ''')
        out.append('</div>')
        return "\n".join(out)
