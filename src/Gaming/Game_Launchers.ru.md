---
title: Игровые лаунчеры
---

# Игровые лаунчеры

## Настройка Steam

Steam может запускать Windows-игры в Linux. Для совместимости с Windows он использует множество проектов и патчей, собранных в компонент Steam под названием [**Proton**](https://github.com/ValveSoftware/Proton). Подробнее можно прочитать [здесь](/Gaming/gaming-intro/#steam-games).

### Принудительный выбор конкретной версии Proton / Steam Play Tool

#### Важные примечания

- Игры с Linux-версией по умолчанию будут использовать ее на Desktop-образах.
- На образах _Handheld/HTPC_ стандартный раннер выбирает Valve.
- Некоторые игры лучше работают с конкретной версией Proton, чем с Linux-версией, хотя иногда бывает и наоборот.

Чтобы запустить игру с конкретной версией, откройте **Properties** → **Compatibility**, включите **Force the use of a specific Steam Play compatibility tool** и выберите нужный вариант в раскрывающемся меню.

!!! warning "Используйте **только** нативную Linux-версию Counter Strike 2, то есть ОТКЛЮЧИТЕ **Force the use of a specific Steam Play compatibility tool**. За запуск CS2 через Proton можно получить VAC-бан."

#### Пример на изображениях

![Cog Icon > Properties|690x284, 75%](../img/Steam_Setup_Cog.png)
![Compatibility tab|690x492, 75%](../img/Steam_Setup_Compat_Tab.png)


## Игры вне Steam

Вы можете использовать Lutris (предустановлен) или другие лаунчеры, например [**Heroic Games Launcher**](https://flathub.org/en/apps/com.heroicgameslauncher.hgl) (для игр GOG/Epic/Amazon) и [**Faugus**](https://flathub.org/en/apps/io.github.Faugus.faugus-launcher), чтобы управлять Proton-префиксами, версиями Proton Runner и [параметрами запуска](/Gaming/launch-options-env-variables/) для игр вне Steam.

!!! note "Другие лаунчеры можно установить через **Bazaar**."

!!! info "Игры вне Steam также можно добавить в Steam и позволить Steam управлять их префиксами. Это полезно в Steam Gaming Mode."

### Настройка

Обычно достаточно указать расположение игры через параметр **Add locally installed game**. После этого Proton-префикс будет создан, а выбранный лаунчер начнет управлять им автоматически. Если вы хотите сами управлять расположением префикса, выберите соответствующие параметры в нужном лаунчере.

!!! note "Lutris предлагает два способа запускать Windows-игры на Bazzite: скрипты сообщества или ручное добавление исполняемого файла. **Настоятельно рекомендуется использовать ручной способ**, так как некоторые скрипты плохо поддерживаются."

### Ручное добавление Windows-игры в Lutris

!!! note

    Большинство других лаунчеров настраиваются похожим образом, как описано ниже.

![Add Locally Installed Game|632x496, 75%](../img/Lutris_Setup_Add_Local_Game.png)

![Lutris manually adding games example 1|690x213](../img/Lutris_Setup_Add_Local_Game_1.png)

По умолчанию Lutris использует каталог `~/Games` для [**каталога префикса**](/Gaming/Managing_and_modding_games/#what-is-a-proton-or-wine-prefix) каждой игры.

### Добавление ярлыков и записей рабочего стола

![Lutris_Right_Click_Menu|421x447, 75%](../img/Lutris_Setup_Shortcut.png)

Ярлык игры можно добавить в меню приложений или на рабочий стол через вкладку редактирования либо контекстное меню правой кнопки мыши в выбранном лаунчере. Выберите там соответствующие пункты.
