---
title: Swap для додаткової пам'яті або гібернації
---

# Swap для додаткової пам'яті або гібернації

## Призначення { #purpose }

Цей посібник покроково пояснює, як створити файл підкачки (swapfile) у файловій системі BTRFS. Його можна використовувати як додаткову пам'ять або для гібернації.

Образи Bazzite-Deck уже підтримують гібернацію через Handheld Daemon за допомогою динамічного файлу підкачки (`General -> Hibernate`). Крім того, усі образи Bazzite за замовчуванням використовують zram, щоб надати додаткову пам'ять.

Скористайтеся цим посібником, якщо хочете створити постійний файл підкачки замість zram, щоб мати більше нестисненої пам'яті, або якщо хочете користуватися гібернацією через робоче середовище.

## Створення файлу підкачки { #create-the-swapfile }

Спершу створіть підтом (subvolume) для файлу підкачки. Тоді, якщо ви вирішите користуватися знімками, файл підкачки не потраплятиме в них. Також треба виправити контекст SELinux для теки з файлом підкачки.
```bash
sudo btrfs subvolume create /var/swap
sudo semanage fcontext -a -t var_t /var/swap
sudo restorecon /var/swap
```

Потім створіть сам файл підкачки. У цьому прикладі ми створюємо файл підкачки на 26 ГБ. Знову ж таки, треба виправити контекст SELinux для самого файлу підкачки.
```bash
SIZE=26G
sudo btrfs filesystem mkswapfile --size $SIZE /var/swap/swapfile
sudo semanage fcontext -a -t swapfile_t /var/swap/swapfile
sudo restorecon /var/swap/swapfile
```

Увімкніть файл підкачки, щоб перевірити, що він працює:
```bash
sudo swapon /var/swap/swapfile
```

## Додавання у fstab { #adding-it-to-fstab }
Тепер треба додати файл підкачки в `/etc/fstab`, щоб він вмикався постійно:
```
sudo cp /etc/fstab /etc/fstab.bak
sudo nano /etc/fstab
```

!!! attention
    Будьте обережні, коли редагуєте файл fstab, **інакше система більше не запуститься**! У такому разі для завантаження можна скористатися попереднім образом.

Додайте у fstab такий **рядок**:

```
/var/swap/swapfile none swap defaults,nofail 0 0
```

## Вимкнення zram { #disable-zram }
Нарешті, щоб гібернація працювала правильно, треба вимкнути zram. Для цього можна очистити файл конфігурації zram-generator. Тоді оновлення Bazzite його не відновлять.
```
echo "" | sudo tee /etc/systemd/zram-generator.conf
```

Насамкінець перезавантажте пристрій, щоб застосувати зміни.

## Скасування змін і відновлення zram { #reverting-changes-and-restoring-zram }
Щоб скасувати зміни й відновити zram, спершу видаліть запис про файл підкачки з `/etc/fstab`. Потім знову ввімкніть zram, скопіювавши назад оригінальний файл конфігурації:
```
sudo cp /usr/etc/systemd/zram-generator.conf /etc/systemd/zram-generator.conf
```
