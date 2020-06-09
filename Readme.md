## Pure Color Video

To generate 5 seconds of pure red video using lavfi `color` source:

```sh
ffmpeg -filter_complex 'color=c=red' -t 5 out.mkv
```

Scripts to generate 5 seconds of pure color video with resolution of 1920x1080:

```sh
#!/bin/bash
ffmpeg -s 1920x1080 -aspect 1.7777 -filter_complex "color=c='$1'" -t 5 $1.mp4
```

# Reference

 - [ffmpeg Documentation](https://ffmpeg.org/ffmpeg.html)
