# pywal-reddit
Downloads images from reddit and sets them as wallpaper via pywal

## Dependencies
[PyWal](https://github.com/dylanaraps/pywal)
## How to use
### From terminal
Run (Dark mode)
```
python pywal-reddit.py wallpapers
```
Run (Light mode)
```
python pywal-reddit.py wallpapers lightmode
```
### With rofi-menu
```
~/pywal-reddit/./rofi-menu.sh
```
### Bind rofi-menu i3 hotkey
```
echo "bindsym \$mod+t exec --no-startup-id ~/pywal-reddit/rofi-menu.sh" >> testconf
```
Then reload i3 config
