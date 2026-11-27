"""Split the unified search index into per-language indexes."""

import json
import os
from copy import deepcopy

from mkdocs.plugins import event_priority


@event_priority(-200)
def on_post_build(config, **kwargs):
    site_dir = config["site_dir"]
    index_path = os.path.join(site_dir, "search", "search_index.json")

    if not os.path.exists(index_path):
        return

    # Read the language list from the i18n plugin config
    i18n_plugin = config["plugins"].get("i18n")
    if i18n_plugin is None:
        return

    languages = [lang["locale"] for lang in i18n_plugin.config["languages"]]
    default_lang = next(
        lang["locale"]
        for lang in i18n_plugin.config["languages"]
        if lang.get("default")
    )

    with open(index_path, encoding="utf-8") as f:
        data = json.load(f)

    # Group docs by language based on location prefix
    docs_by_lang = {lang: [] for lang in languages}
    for doc in data["docs"]:
        location = doc["location"].lstrip("./")
        matched = False
        for lang in languages:
            if lang == default_lang:
                continue
            if location == lang:
                location = ""
            elif location.startswith(f"{lang}/"):
                location = location[len(lang) +1:]
                # Strip the language prefix so relative paths work
                # from within the language subdirectory
            else:
                continue
            stripped = deepcopy(doc)
            stripped["location"] = location
            docs_by_lang[lang].append(stripped)
            matched = True
            break
        if not matched:
            docs_by_lang[default_lang].append(doc)

    # Write per-language indexes for non-default languages
    for lang in languages:
        if lang == default_lang:
            continue
        if not docs_by_lang[lang]:
            continue

        lang_index_path = os.path.join(site_dir, lang, "search", "search_index.json")
        os.makedirs(os.path.dirname(lang_index_path), exist_ok=True)

        lang_config = deepcopy(data["config"])
        lang_config["lang"] = [lang]

        with open(lang_index_path, "w", encoding="utf-8") as f:
            json.dump(
                {"config": lang_config, "docs": docs_by_lang[lang]},
                f,
                ensure_ascii=False,
            )

    # Overwrite the root index with only the default language
    default_config = deepcopy(data["config"])
    default_config["lang"] = [default_lang]

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(
            {"config": default_config, "docs": docs_by_lang[default_lang]},
            f,
            ensure_ascii=False,
        )
