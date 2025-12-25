# Hyprland Testing

## Dotfile?

Just got curious and tested hyprland, hehe, but messed up really badly. The interesting dotfile,

- <https://ii.clsty.link/en/>
- <https://github.com/end-4/dots-hyprland>

### And,

some extra config I did,

```
# Put general config stuff here
# Here's a list of every variable: https://wiki.hyprland.org/Configuring/Variables/

# monitor=,addreserved, 0, 0, 0, 0 # Custom reserved area
monitor=eDP-1,preferred,0x0,1.0

# HDMI port: mirror display. To see device name, use `hyprctl monitors`

# Input settings
input {
    kb_layout = us,bd
    kb_options = grp:win_space_toggle
    numlock_by_default = true
    repeat_delay = 250
    repeat_rate = 35

    follow_mouse = 1
    off_window_axis_events = 2

    touchpad {
        natural_scroll = yes
        disable_while_typing = true
        clickfinger_behavior = true
        scroll_factor = 0.7
    }
}
# Put general config stuff here
# Here's a list of every variable: https://wiki.hyprland.org/Configuring/Variables/

# monitor=,addreserved, 0, 0, 0, 0 # Custom reserved area

# HDMI port: mirror display. To see device name, use `hyprctl monitors`

# Input settings
input {
    kb_layout = us,bd
    kb_options = grp:win_space_toggle
    numlock_by_default = true
    repeat_delay = 250
    repeat_rate = 35

    follow_mouse = 1
    off_window_axis_events = 2

    touchpad {
        natural_scroll = yes
        disable_while_typing = true
        clickfinger_behavior = true
        scroll_factor = 0.7
    }
}
```

It was to add my bangla keyboard and monitor scaling, no big deal ;)

## Update user directory

Creating entries for the directories.

```bash
xdg-user-dirs-update
```

## Time and Date

Using `timedatectl` to update time and date.

- <https://www.wikihow.com/Change-the-Timezone-in-Linux>

## Apps

- speech dispatcher service
