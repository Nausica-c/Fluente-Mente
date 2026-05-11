import os
import yaml
import random
from slugify import slugify

# ============================================
# FLUENTEMENTE CLUSTER FACTORY
# ============================================

POSTS_DIR = "_posts"
DATA_FILE = "data/clusters.yaml"

# crea cartella posts
os.makedirs(POSTS_DIR, exist_ok=True)

# ============================================
# LOAD YAML
# ============================================

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

# ============================================
# TEMPLATE TITLES
# ============================================

TITLE_PATTERNS = [
    "Come imparare inglese con il metodo {topic}",
    "Il metodo migliore per migliorare {topic}",
    "Perché non riesci a parlare inglese",
    "Come sbloccare il tuo inglese in modo naturale",
    "Il sistema più semplice per imparare inglese",
    "Come allenare speaking ogni giorno",
    "Il metodo dei 15 minuti per l'inglese",
    "Come imparare inglese senza studiare grammatica",
    "Il problema dei corsi tradizionali",
    "Come pensare direttamente in inglese"
]

TOPICS = [
    "speaking",
    "fluency",
    "vocabolario",
    "ascolto",
    "pronuncia",
    "conversazione",
    "mindset",
    "routine"
]

# ============================================
# CTA ENGINE
# ============================================

def generate_cta():
    return {
        "title": "🚀 Inizia a parlare davvero",
        "text": "Allenati ogni giorno con un metodo guidato.",
        "button": "Prova Babbel gratis →",
        "variant": "primary"
    }

# ============================================
# PINTEREST ENGINE
# ============================================

def generate_pinterest():
    return {
        "enabled": True,
        "pins_min": 6,
        "pins_max": 20,
        "angles": [
            "problema",
            "errore",
            "soluzione rapida",
            "metodo segreto"
        ]
    }

# ============================================
# ARTICLE BODY
# ============================================

def generate_body(title):

    return f"""
# {title}

Imparare inglese non significa studiare ore di grammatica.

Molte persone rimangono bloccate perché usano un metodo sbagliato.

## Il vero problema

Il problema spesso non è la memoria.

È il sistema.

## Cosa funziona davvero

- pratica quotidiana
- speaking reale
- immersione
- ripetizione naturale

## Come migliorare più velocemente

Usare micro-sessioni quotidiane aiuta a creare continuità.

Anche 15 minuti al giorno possono fare differenza.

{{% include components/cta/cta-primary.html %}}

## Conclusione

La costanza conta più della perfezione.
"""

# ============================================
# FRONTMATTER
# ============================================

def generate_frontmatter(title, slug, cluster):

    return {
        "layout": "post",
        "title": title,
        "slug": slug,
        "permalink": f"/inglese/{cluster}/{slug}/",

        "language": "en",
        "language_target": "english",

        "type": "method",
        "cluster": cluster,
        "subcluster": "base",

        "intent_level": random.choice([
            "soft",
            "medium",
            "hard"
        ]),

        "meta_title": title,
        "meta_description": f"Guida pratica: {title}",

        "content_pillar": "foundation",

        "difficulty": "beginner",

        "content_goal": "speaking",

        "related_cluster": cluster,

        "parent_hub": f"/inglese/{cluster}/",

        "bridge_target": "babbel",

        "cta_primary": generate_cta(),

        "affiliate": {
            "enabled": True,
            "partner": "babbel"
        },

        "pinterest": generate_pinterest(),

        "funnel_stage": "TOFU",

        "show_tldr": True,
        "show_quote": True,
        "show_warning": False,
        "show_trust_box": True,

        "ai_generated": True
    }

# ============================================
# GENERATE ARTICLES
# ============================================

languages = data["languages"]

for language_name, language_data in languages.items():

    clusters = language_data["clusters"]

    for cluster_name, cluster_data in clusters.items():

        if not cluster_data.get("enabled"):
            continue

        article_count = cluster_data.get("article_count", 10)

        print(f"\n🚀 Generating cluster: {cluster_name}")

        for i in range(article_count):

            title_template = random.choice(TITLE_PATTERNS)
            topic = random.choice(TOPICS)

            title = title_template.format(topic=topic)

            slug = slugify(title)

            frontmatter = generate_frontmatter(
                title,
                slug,
                cluster_name
            )

            body = generate_body(title)

            filename = f"2026-05-{str(i+1).zfill(2)}-{slug}.md"

            filepath = os.path.join(
                POSTS_DIR,
                filename
            )

            with open(filepath, "w", encoding="utf-8") as f:

                f.write("---\n")
                yaml.dump(
                    frontmatter,
                    f,
                    allow_unicode=True,
                    sort_keys=False
                )
                f.write("---\n")
                f.write(body)

            print(f"✅ Created: {filename}")

print("\n🎉 FluenteMente generation completed.")
