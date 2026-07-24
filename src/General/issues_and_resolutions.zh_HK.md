---
title: 疑難排解
---

# 疑難排解

## Steam Big Picture 模式十分卡頓

當使用**左上角的 Steam Menu → 檢視 → Big Picture 模式**進入 Steam Big Picture 模式時，介面十分甚至九分卡頓，但遊戲運行沒有問題。

如你遇到此問題，請退出 Steam ，並使用系統搜尋或應用程式目錄內的 **Steam Big Picture 模式**捷徑啟動 Steam 。此外，確保 **Steam 設定 → 介面 → 「在網頁瀏覽中啟用GPU加速彩現（需要重新啟動）」**為「開啟」。

>此解亦適用於 Nvidia 顯卡在 Steam 遊戲模式內的卡頓情況，但亦有機會導致顯示錯誤，如目錄無法正常顯示等。

<hr>

## 在華碩 ROG Ally 系列產品中，在最大音量下，實際音量仍十分細小

在 ROG Ally 系列中，系統會辨識到兩個音訊控制器：

-   **Family 17h/19h/1ah HD Audio Controller**
-   **ROG Ally**

兩者皆影響全域音量，請確保兩者音量設定一致。

<hr>

## 於桌面模式中無法使用手柄／控制器的搖桿

打開 **Steam 設定→控制器→非遊戲控制器配置→桌面配置**。點選「編輯」，並設置你的手柄／控制器如何在桌面模式下模擬鍵盤和滑鼠操作。

!!! Tip "你或需降低**右搖桿靈敏度**至50-80%。"

!!! 溫馨提示 "於 KDE Plasma 6.7 版本中， Plasma 新增了透過手柄控制桌面的功能。此功能會與 Steam 的**非遊戲控制器配置→桌面配置**衝突。若你想使用Plasma原生的手柄功能，請記得關閉 Steam 內的**非遊戲控制器配置**選項。"

## 在Bazzite桌面版設置自動登入

=== "KDE Plasma"

    打開 **System Settings → Colors and Themes → Login Screen** 並點選 **Automatically log in** ，然後選擇你的用戶名，並於 session 選單內點選 **Plasma** 。別忘記點擊 **Apply** 按鈕！
    
=== "GNOME"

    打開 **Settings application → Users** 並點選右上角的 **Unlock** 按鈕，然後開啟 **Automatic Login** 。

<hr>

## 在舊GPU上設置類Steam遊戲模式

由於一些顯卡不支持運行 Steam 遊戲模式，以下列出在 Bazzite 桌面版塑造類 Steam 遊戲模式的操作：

設置自動登入，然後將 Steam Big Picture 模式加入系統自啟動列表。<small>_就這！？_</small>

<hr>

## 在Windows與Bazzite雙啟動時，Bazzite無法訪問網路

這很大機會是因為 Windows Fast Startup 。Windows Fast Startup 為縮短開機時間，會將你的電腦卡進一個介於關機與休眠（Suspend-to-disk、Hibernation）的狀態之中。這個狀態會使大部份外設裝置無法被其他作業系統存取。你可以在 Windows 內**重新啟動**以進行一個完整的 Power Cycle 以避免這個狀態，但長遠來説，**關閉 Windows Fast Startup **是一個比較好的選項。

-   打開 **Control Panel**
-   點選 **Hardware and Sound**
-   點選 Power Options → **Change what the power buttons do**
-   點選 **Change settings that are currently unavailable**
-   關閉 **Turn on fast startup (recommended)**
-   (可選) 關閉 **Hibernate**
-   點擊 **Save changes**

<hr>

![how to disable fast startup in Windows](../img/disable-windows-fast-startup.gif)

## Wi-Fi網速低、延遲高

某些裝置的 Wi-Fi 節能模式在 Linux 上未必完善，你可以嘗試關閉 Wi-Fi 節能模式以改善網路質素。如你在Bazzite的網速、網路情況（僅限Wi-Fi）顯著地差於 Windows ，那你可以嘗試以下解決辦法。

打開系統終端（Terminal），並輸入 `ip link show` 指令，系統會以類似以下格式列出所有網絡裝置：

```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: wlp6s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DORMANT group default qlen 1000
    link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff permaddr 00:00:00:00:00:00
```

注意你的 Wi-Fi 網卡名稱－以上圖為例，網卡名稱為 `wlp6s0` 。

!!! tip "另一種常見的網卡名稱為 `wlan0` 。"

輸入 `iw wlp6s0 get power_save` 指令 （記得把 `wlp6s0` 替換成你的網卡名稱！）以查看節能模式的狀態：
```
Power save: on
```

輸入以下指令以設置 NetworkManager 為不使用 Wi-Fi 節能模式：

```bash
echo -e "[connection]\nwifi.powersave = 2" | sudo tee /etc/NetworkManager/conf.d/wifi-powersave-off.conf
systemctl restart NetworkManager
```

輸入 `iw wlp6s0 get power_save` 指令，確認節能模式已關閉：

```
Power save: off
```
!!! warning "此設置或會縮短裝置的續航時長"

如需撤銷此設置，請輸入以下指令以移除設置檔文件：
```bash
sudo rm /etc/NetworkManager/conf.d/wifi-powersave-off.conf
systemctl restart NetworkManager
```

<hr>

## 更改 Wi-Fi 後端

!!! 額外資訊 "由於 [Intel 的內部政策轉變，其不再著重於開源軟體及項目](https://www.phoronix.com/review/intel-open-source-2025)，他們的 [`iwd`](https://wiki.archlinuxcn.org/wiki/Iwd) 項目亦不再受到維護。你暫時仍可嘗試使用 [`iwd`](https://wiki.archlinuxcn.org/wiki/Iwd) 修復 [`wpa_supplicant`](https://wiki.archlinuxcn.org/wiki/Wpa_supplicant) 帶來的連線質量問題，但 [`iwd`](https://wiki.archlinuxcn.org/wiki/Iwd) 將於不遠的未來被移除。有鑑於此，Bazzite仍建議你將 Wi-Fi 後端設定為 [`iwd`](https://wiki.archlinuxcn.org/wiki/Iwd)。"

開啟 [Bazzite Portal](/Installing_and_Managing_Software/Bazzite_Portal/)，在 **Troubleshooting** 分頁，點選 **Change Wi-Fi system back-end** 。

<hr>

## 裝置未能偵測 Nvidia Optimus（優馳）

若你正在有 Nvidia Optimus 支持的裝置（如 Intel+Nvidia 筆記本）上運行 Bazzite，而性能未達預期，且遊戲疑似運行於iGPU（核顯）之上，你便需要採取以下措施：

輸入以下指令以開啟 `supergfxctl` ：

```bash
ujust enable-supergfxctl
```

!!! info "如果你正在尋找**高級Optimus功能**，Bazzite 只能遺憾地告訴你目前除了AMD SmartMUX於內核中的早​​期開發工作之外，**沒有**方法能夠對顯卡進行動態MUX切換。目前你**必須**重新啟動系統以更改MUX設定。"

<hr>

## 於 Nvidia 裝置上， Flatpak 應用程式失去了硬件加速功能

在 Nvidia 裝置上，如 Bazzite 在近期曾有更新，你的 Flatpak 應用程式或會失去硬件加速，且你或會收到一個「**Nvidia Flatpak Runtime mismatch**」的通知。

別擔心，一切安好。你只需於 **Bazaar 應用商店** 中更新所有程式及運行環境。若你只想更新 Nvidia 的 Flatpak 運行環境，你亦可於 **Bazzite Portal** → **Manage Bazzite** 分頁中選取 **Update Nvidia Flatpak Runtime**。

!!! info "Bazzite已預先設定了一個Systemd服務以自動更新這些運行環境，但在一些情況下（如在開機時無網絡連接），此服務會失效，而你需進行手動更新。理論上的最佳解決辦法為在上游的 Nvidia/Flatpak 不再使用獨立的版本管理這些運行環境，或是創建一個包含 Flatpak 運行環境的系統包；但俗話「講就容易，做就難」，事到如今 Bazzite 也只能盡量縮小此問題帶來的影響。"

<hr>

## 技嘉主板無法從睡眠中甦醒

<small>_生命因何而沉睡？ ...因為技嘉主板無法從睡眠中醒來。_</small>

鵰牌的主板在進入睡眠模式之後，其有機會無法正常恢復且在重啟前僅會顯示黑屏，而此問題可透過關閉GPP0及GPP8甦醒來解決。為此，Bazzite 提供一個隱藏的指令：

```bash
ujust _toggle-gigabyte-wake-fix
```

<hr>

## Xbox控制器的Xbox按鈕發出閃光，且無法透過藍牙連線

這是因為你的控制器在運行舊版韌體。若你能將其連接至Windows電腦，你可以下載Xbox Accessories應用程式並更新韌體。

你亦可創建一個Windows虛擬機，並設置Passthrough至該虛擬機，然後更新韌體。

<hr>

## 我的鼠標在閃爍／消失了

這一般源自顯卡驅動的Bug，你可以關閉硬體鼠標以暫時修復此問題。

=== "KDE Plasma"

    輸入以下指令以添加環境函數：

    ```bash
    echo "KWIN_FORCE_SW_CURSOR=1" > ~/.config/environment.d/99-kwin-force-sw-cursor.conf
    ```

=== "GNOME"

    輸入以下指令以添加環境函數：

    ```bash
    echo "MUTTER_DEBUG_DISABLE_HW_CURSORS=1" > ~/.config/environment.d/99-mutter-disable-hw-cursor.conf
    ```

!!! warning "此設置或會縮短裝置的續航時長"

## 無法開啟 Dolphin 的 SMB Share 功能

這是因為原子化系統存取 Usergroup 的位置與 Dolphin 預期的位置不同，所以你的用戶無法透過 Dolphin 介面上的按鈕加入 usershares 組別。

將 `<username>` 替換成你的用戶名，然後運行以下指令：
```bash
grep -E '^usershares:' /usr/lib/group | sudo tee -a /etc/group
sudo usermod -aG usershares <username>
```
