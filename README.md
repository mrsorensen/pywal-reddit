# pywal-reddit
Downloads images from reddit and sets them as wallpaper via pywal
## Screenshots
![From terminal](https://github.com/mrsorensen/pywal-reddit/blob/master/screenshots/screen1.png)
![With rofi-menu](https://github.com/mrsorensen/pywal-reddit/blob/master/screenshots/screen2.png)
## Dependencies
[PyWal](https://github.com/dylanaraps/pywal)
## How to use
### From terminal
Run (Dark mode)
```
python ~/pywal-reddit/pywal-reddit.py wallpapers
```
Run (Light mode)
```
python ~/pywal-reddit/pywal-reddit.py wallpapers lightmode
```
### With rofi-menu
```
~/pywal-reddit/./rofi-menu.sh
```
### Bind rofi-menu i3 hotkey
```
echo "bindsym \$mod+t exec --no-startup-id ~/pywal-reddit/rofi-menu.sh" >> ~/.config/i3/config
```
Then reload i3 config
