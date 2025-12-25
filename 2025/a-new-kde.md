# A New Kde

Things in this file are not organized properly, so maybe I will cover it in the blog site :)

## Update tracker

Adaptifier gets you covered!
- <https://store.kde.org/p/2135796/>
- <https://github.com/exequtic/apdatifier> - [HOMEPAGE]

## Theming

Check `darkly`
- <https://aur.archlinux.org/packages/darkly-bin>

## Icon

For icon packs, `papirus` does a great job, I guess :)


# Check...

## Login manager

sddm-git, also check, 
- <https://wiki.archlinux.org/title/SDDM>

If you are facing issues like, 
configuration file of greeter is not writable, 
then execute the following line,

```bash
sudo chown -R sddm:sddm /var/lib/sddm/.config
```
and `reboot`.

## Office

Libreoffice or only office is recommended from me, pick whatever you feel comfortable with :)

## Media player

vlc with all optional deps/ haruna. It's better to install the one that you will use most later, for overriding defaults.

## YouTube 
`yt-dlp` should be enough.

## Text editor

kate/ zeditor - or vscode

# System

## Fonts

`ttf-ms-fonts` - microsoft fonts

## Swap

For setting up swap, an awesome guideline will be,
- <https://wiki.manjaro.org/index.php?title=Swap>

## TTS

Check this article,
- <https://wiki.archlinux.org/title/Speech_dispatcher>

> Just installing `speech-dispatcher` and `espeak-ng` should do the trick!

## Mirror Ranking

For mirror ranking, `rate-mirrors` from AUR does the job just fine.
