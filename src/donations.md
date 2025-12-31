---
title: Credits and Donating
---

# Credits and Donating

{% macro contributor(real_name, github, description, sponsor) -%}
    <div style="
    display: inline-flex;
    flex-direction: row;
    gap: 0.5rem;
    align-items: top;
    background-color: #00000066;
    border-radius: 24px;
    padding: 0.3rem;
    padding-right: 0.4rem;
    min-width: 200px;
    width: 100%;
    max-width: 335px;
    line-height: 1.1rem;"
    >
        {% if github %}
            <img
            src="https://github.com/{{ github }}.png?size=60" class="no-lightbox"
            loading="lazy"
            style="max-height:60px;
                border-radius: 24px;"
            >
        {% endif %}
        <div>
            {% if github %}
                <a href="https://github.com/{{ github }}">{{ real_name }}</a>
            {% else %}
                <span>{{ real_name }}</span>
            {% endif %}
            {% if sponsor %}
                <small>
                  <a
                    href="{{ sponsor }}"
                    style="
                      background-color: var(--md-primary-fg-color);
                      color: var(--md-primary-bg-color);
                      border: none;
                      padding: 1px 3px;
                      border-radius: 24px;"
                  >Sponsor</a>
                </small>
            {% endif %}
            <div><small>{{ description or "" }}</small></div>
        </div>
    </div>
{%- endmacro %}

Love Bazzite and want to help sustain its development?

<div class="button-container">
    <a href="https://opencollective.com/bazzite-us" target="_blank" class="sponsor-button">Sponsor Bazzite ($ USA)</a>
    <a href="https://opencollective.com/bazzite-eu" target="_blank" class="sponsor-button">Sponsor Bazzite (€ Europe)</a>
</div>


## Projects Included in Bazzite

<Need something like [Bluefin](https://docs.projectbluefin.io/donations)>
