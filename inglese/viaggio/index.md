---
layout: cluster
title: "Inglese per viaggiare senza stress"
description: "Tutte le frasi, situazioni e guide per comunicare in inglese durante i viaggi."
cluster: viaggio
cta_level: soft
permalink: /inglese/viaggio/
---

{% assign cluster = site.data.viaggio %}

# ✈️ Inglese per viaggiare

{% include article/cta-soft.html %}

---

## 🧭 Esplora il cluster

{% for section_key in cluster.sections %}

  {% assign section = cluster.sections[section_key] %}

  ## {{ section.title }}

  <ul>

    {% for article in section.articles %}

      <li>
        <a href="{{ article.url }}">
          {{ article.title }}
        </a>
      </li>

    {% endfor %}

  </ul>

{% endfor %}

---

## 🚀 Perché questo cluster esiste

Imparare inglese per viaggiare non significa studiare grammatica,  
ma saper reagire nelle situazioni reali.

---

## 🌍 Cosa trovi qui

- Aeroporto
- Hotel
- Ristorante
- Situazioni reali
- Viaggi quotidiani

---

{% include article/cta-mid.html %}
