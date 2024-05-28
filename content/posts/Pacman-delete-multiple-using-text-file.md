+++
title = "Pacman-delete-multiple-using-text-file"
description = "This command did the trick, but it's not perfect. It will fail if the package is a dependency of another package."
+++

# Pacman delete multiple using text file

This command did the trick, but it's not perfect. It will fail if the package is a dependency of another package.

```bash
while read -r package version; do
    sudo pacman -Rns --noconfirm "$package"
done < Desktop/fonts.txt
```

My text file was,

```text
ttf-agave-nerd 3.1.1-1
ttf-anonymouspro-nerd 3.1.1-1
ttf-arimo-nerd 3.1.1-1
ttf-bigblueterminal-nerd 3.1.1-1
ttf-bitstream-vera-mono-nerd 3.1.1-1
ttf-cascadia-code-nerd 3.1.1-1
ttf-cousine-nerd 3.1.1-1
ttf-daddytime-mono-nerd 3.1.1-1
ttf-dejavu-nerd 3.1.1-1
ttf-fantasque-nerd 3.1.1-1
ttf-go-nerd 3.1.1-1
ttf-heavydata-nerd 3.1.1-1
ttf-iawriter-nerd 3.1.1-1
ttf-ibmplex-mono-nerd 3.1.1-1
ttf-inconsolata-go-nerd 3.1.1-1
ttf-inconsolata-lgc-nerd 3.1.1-1
ttf-inconsolata-nerd 3.1.1-1
ttf-iosevka-nerd 3.1.1-1
ttf-iosevkaterm-nerd 3.1.1-1
ttf-lekton-nerd 3.1.1-1
ttf-liberation 2.1.5-1
ttf-liberation-mono-nerd 3.1.1-1
ttf-lilex-nerd 3.1.1-1
ttf-meslo-nerd 3.1.1-1
ttf-monofur-nerd 3.1.1-1
ttf-monoid-nerd 3.1.1-1
ttf-mononoki-nerd 3.1.1-1
ttf-mplus-nerd 3.1.1-1
ttf-nerd-fonts-symbols 3.1.1-1
ttf-nerd-fonts-symbols-common 3.1.1-1
ttf-nerd-fonts-symbols-mono 3.1.1-1
ttf-noto-nerd 3.1.1-1
ttf-opensans 1.101-2
ttf-profont-nerd 3.1.1-1
ttf-proggyclean-nerd 3.1.1-1
ttf-roboto-mono-nerd 3.1.1-1
ttf-sharetech-mono-nerd 3.1.1-1
ttf-sourcecodepro-nerd 3.1.1-1
ttf-space-mono-nerd 3.1.1-1
ttf-terminus-nerd 3.1.1-1
ttf-tinos-nerd 3.1.1-1
ttf-victor-mono-nerd 3.1.1-1

```

