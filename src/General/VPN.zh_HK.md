---
title: 使用 VPN
---

# 使用 VPN

## 使用可正常運作的 VPN Flatpak 軟件包

由於 Flatpak 的沙盒化相當嚴苛，大部分 VPN 客戶端都不提供 Flatpak 軟件包，因此你將不能在 Bazaar 應用商店中找到它們。話雖如此，以下的 VPN 仍有在 Bazaar 應用商店中提供客戶端軟件：

- [Mozilla VPN](https://flathub.org/zh-Hant/apps/org.mozilla.vpn)
- [ProtonVPN](https://flathub.org/zh-Hant/apps/com.protonvpn.www) <small>注：非官方安裝包</small>

## 使用 Tailscale

為提供內網穿透，及為桌面和開發用途，Bazzite 已預安裝 Tailscale。Bazzite建議你先閱讀這個 [Tailscale 教程](https://blog.6nok.org/tailscale-is-pretty-useful/)。

-   [以 Tailscale 連接 Mullvad VPN](https://tailscale.com/kb/1258/mullvad-exit-nodes) - 若你只需使用 VPN 以繞過網絡地理限制，這是最簡單的使用方法。
  -   [在 Docker 容器中使用 Tailscale](https://tailscale.com/kb/1282/docker) - 作開發用途。
  -   **Bazzite Portal** 中的「Enable Tailscale」選項將移除內建的桌面功能，以供你使用其他的桌面 Tailscale 客戶端。
  -   Tailscale 的 [YouTube 頻道](https://www.youtube.com/@Tailscale) 提供不少指引和小貼士。
-   一般來説，優質的 VPN 服務會提供一個可直接匯入 NetworkManager 的 WireGuard 設定檔，請參閱你的 VPN 服務供應商的說明文件以獲取更多資訊。
-   請僅在萬不得已時，才使用 [`rpm-ostree` 疊加 VPN 安裝包。](/Installing_and_Managing_Software/rpm-ostree/).

## 於桌面環境的設定內匯入 VPN 設定檔

如你不需要 VPN 客戶端提供的某些特殊功能（如「殺手開關」、網絡分流或其他未內建於 VPN 協定中的自訂功能），此選項或許對你來說已經足夠。以這種方式匯入的 VPN 設定檔可供你隨意開啟或關閉。

=== "KDE Plasma"

    1. 打開 System Settings
    2. 前往 Wi-Fi & Internet 分頁，然後點選 "Wi-Fi & Networking"
    3. 點擊在最底的「+」按鈕

    <img src="/img/vpn_settings.png" alt="Settings page of Networking Settings" width="600" height="487" />

    4. 點選你已下載的 VPN 設定檔

    <img src="/img/add_vpn.png" alt="Import VPN config file dialog" width="400" height="617" />

=== "GNOME"

    1. 打開 Settings
    2. 前往 Network 分頁
    3. 點擊在VPN章節中的「+」按鈕

    <img src="/img/vpn_settings_gnome.png" alt="Networking Settings page in GNOME" width="600" height="487" />

    4. 點擊 「Import From file...」

    <img src="/img/add_vpn_file_gnome.png" alt="Import VPN config file dialog in GNOME" width="600" height="487" />

    5. 點選你已下載的 VPN 設定檔
