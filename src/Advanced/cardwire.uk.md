---
title: Cardwire
---

# Cardwire

![Знімок екрана Cardwire|2224x1468, 25%](https://github.com/OpenGamingCollective/cardwire/raw/main/assets/org.opengamingcollective.cardwire.screenshot.png)

## Огляд { #overview }

Cardwire — менеджер відеокарт для Linux, який за допомогою хуків eBPF LSM перехоплює операції з файлами пристроїв відеокарти, як-от `/dev/dri/renderDX`, `/dev/dri/cardX`, `config` у sysfs, `nvidiaX` та інші файли, пов'язані з відеокартою.

Коли відеокарту «заблоковано», програма eBPF повертає -ENOENT на будь-який системний виклик до цього пристрою, тобто фактично приховує його від застосунків. Це дає кілька важливих переваг:

-   Миттєвий запуск застосунків: застосунки (наприклад, на Electron або GTK) не намагаються ініціалізувати відеокарту, тож зникає «зависання» на 3–4 секунди, яке зазвичай виникає, поки сплячу відеокарту вмикають
-   Енергоефективність: оскільки доступ блокується на рівні системних викликів, відеокарта ніколи не виходить зі свого найнижчого стану живлення (D3cold), і ноутбук довше працює від батареї
-   Без втручання в систему: на відміну від традиційних способів, які можуть потребувати вивантаження драйвера, ризикованого відв'язування (unbind) або складного налаштування Wayland, цей підхід непомітний для решти системи, і його легко вмикати й вимикати

!!! note "X11 не підтримується. Cardwire потребує Wayland."

---

## Налаштування { #configuration }

Cardwire можна використовувати через вбудований графічний інтерфейс або через командний рядок.

```console
CLI for cardwire GPU management

Usage: cardwire <COMMAND>

Commands:
set      Set to the desired mode
get      Get the current mode
list     Print the gpu list
gpu      Manage a specific GPU by its id
config   Manage daemon configuration
manager  Manager operations
debug    Debug operations
launch   Launch a program on the specified GPU
help     Print this message or the help of the given subcommand(s)

Options:
-h, --help     Print help
-V, --version  Print version
```

---

## Використання { #usage }

Якщо ви хочете вручну вказати, щоб гра запускалася на певній відеокарті, додайте такий [параметр](../Gaming/launch-options-env-variables.md) до параметрів запуску в Steam:

```bash
cardwire launch %command%
```

!!! note "Інші інструменти керування відеокартами, як-от `switcherooctl`, `envycontrol`, `supergfxctl`, не слід використовувати разом із Cardwire."

> Докладніше — у [документації Cardwire](https://opengamingcollective.github.io/cardwire/).

---

## Сайт проєкту { #project-website }

https://github.com/OpenGamingCollective/cardwire
