---
title: Creating A Custom Bazzite Image
---

# Vytvoření vlastního obrazu Bazzite

## Případy použití

- Chcete vyměnit předinstalované aplikace na systémové úrovni a další výchozí volby, ale chcete se držet blízko Bazzite, aby se vylepšení dostávalo automaticky.
    - Například: Bazzite má Waydroid zapečený do obrazu, ale není nastaven ani spuštěn ve výchozím nastavení.  Pokud si přejete tento balíček odinstalovat, můžete jej nahradit nebo odebrat.
    - Potřebujete navrstvit něco jako software VPN, který musí být v obrazu, ale nechcete udržovat svůj vlastní samostatný obraz. (_Odvozování od ostatních je vždy snazší_)
    - Chcete vlastní obraz pro osobní použití s konfiguračními a softwarovými změnami, ale také chcete těžit z toho, že práce je dokončena proti proudu.
    - Různá desktopová prostředí nebo správci oken oproti tomu, co nabízí Bazzite.
- Chcete pomoci rozvoji Bazzite tím, že budete moci otestovat své příspěvky před odesláním do komunity.
    - Povolení hardwaru, experimentální funkce, potvrzení oprav před sloučením.

## Doporučené metody

### Možnost A – Použití šablony obrazu

Použijte [**oficiální obraz šablony**](https://github.com/ublue-os/image-template), z něhož můžete vytvořit svůj vlastní Bazzite, který má přednost před rozvětvením projektu.

#### Video průvodce

https://www.youtube.com/watch?v=IxBl11Zmq5w

### Možnost B – Forking Bazzite

Někdy nechcete vytvořit úplně nový obraz od začátku, jen chcete změnit některé věci bez přílišné práce navíc **forkingem Bazzite**.  Důrazně se doporučuje používat [**aplikaci Pull pro Github**](https://github.com/apps/pull), aby byl váš fork synchronizovaný.

### Možnost C – Použití BlueBuild

[**BlueBuild**](https://blue-build.org/learn/universal-blue/) je projekt, který původně začal jako výchozí bod pro vytváření vlastních obrazů Universal Blue a nakonec se stal jeho vlastním samostatným projektem.  Veškerá podpora pro obrazy Blue-Build by měla být směrována na příslušné [komunikační kanály](https://blue-build.org/community/) mimo Universal Blue.