+++
title = "Hyperspeedcube"
aliases = ["/hyperspeedcube"]
+++

{{< lead >}}
Multidimensional twisty puzzle simulator
{{< /lead >}}

<a href="{{< ref `/projects/hyperspeedcube` >}}"><img src="https://raw.githubusercontent.com/HactarCE/Hyperspeedcube/main/crates/hyperspeedcube/resources/icon/hyperspeedcube.svg?sanitize=true" alt="Hyperspeedcube logo" width="100" align="right" style="margin: 0px 0px 0px 10px"></a>

Hyperspeedcube is a modern, beginner-friendly 3D and 4D Rubik's cube simulator with customizable mouse and keyboard controls and advanced features for speedsolving. It's been used to break numerous speedsolving records and runs on all major operating systems plus the web.

<!--more-->

[Try it online!](https://hypercubing.xyz/hyperspeedcube/)

If you're new to hypercubing, check out [hypercubing.xyz](https://hypercubing.xyz/), the Hypercubing community website, which I also help maintain.

## Download

{{< button href="https://github.com/HactarCE/Hyperspeedcube/releases/latest/download/hyperspeedcube_win64.zip" >}}{{< icon "windows" >}} Windows{{< /button >}}
{{< button href="https://github.com/HactarCE/Hyperspeedcube/releases/latest/download/hyperspeedcube_linux.tar.gz" >}}{{< icon "linux" >}} Linux{{< /button >}}
{{< button href="https://github.com/HactarCE/Hyperspeedcube/releases/latest/download/hyperspeedcube_macos.tar.gz" >}}{{< icon "apple" >}} macOS{{< /button >}}
{{< button href="https://github.com/HactarCE/Hyperspeedcube/" >}}{{< icon "github" >}} Source code{{< /button >}}

The latest version is {{% release_badge "HactarCE/Hyperspeedcube" %}}

Or see [instructions to build from source](https://github.com/HactarCE/Hyperspeedcube/blob/main/BUILDING.md)

{{% kofi_badge %}}

## Help

See [Hyperspeedcube - Troubleshooting](https://hypercubing.xyz/software/hyperspeedcube/#troubleshooting) and the [FAQ](https://hypercubing.xyz/faq/#hyperspeedcube).

## Screenshots

Click for full resolution.

{{% small_imgur src="rpMgIwp.png" alt="3x3x3x3 with the far cell mid-twist" %}}
{{% small_imgur src="uDzvYLz.png" alt="3x3x3x3 near the end of F2L-b with many tools and settings windows open" %}}
{{% small_imgur src="aAVOjsD.png" alt="Solved 2x2x2" %}}
{{% small_imgur src="q1CFcri.png" alt="3x3x3 superflip" %}}
{{% small_imgur src="jWmiZIG.png" alt="3x3x3x3 with the back cell mid-twist" %}}
{{% small_imgur src="XAH18Lo.png" alt="Solved 3x3x3x3 with 2c pieces highlighted and stickers on the same piece connected" %}}

## Testimonials

> also, huge shoutout to hactar!! the hyperspeedcube program is way better than it has any right to be, like hello?? how is it so goated???

> and heres the thing, he's working on a 2.0 version thats going to be infinitely better

> I *highly* recommend Hyperspeedcube if you want to do 5^4. The piece filters menu even without any presets will make a world of difference.

> if you can use it, a lot of us would recommend hyperspeedcube rather than MC4D these days, since it has more features to make things easier/more approachable, and is generally a more modern program

> Half of the pain of this program is you expect it to be bad, and it's actually good, so you try to work around a problem that's already solved

## Features

- Supports several puzzles
  - 3D Rubik's cube from 1x1 up to 9x9
  - 4D "Rubik's hypercube" from 1x1 up to 9x9
- Import/export using `.hsc` or MC4D-compatible `.log` file
- Mouse and keyboard controls for all puzzles, with multiple keybind sets
- Filter which pieces are visible, with presets
- Mark pieces to track as they move
- _Everything_ is customizable
  - Keybinds
  - Mouse controls
  - Colors
  - Opacity
  - Animation speed
  - 3D and 4D projection settings
  - Lighting

## How to use

Hyperspeedcube has completely customizable mouse and keyboard controls. By default:

- Left click to rotate a face counterclockwise
- Right click to rotate a face clockwise
- Middle click to recenter a face
- See **Help → Keybinds reference** for keybinds

The keyboard controls for the 3D Rubik's cube are mostly based on [Ryan Heise's speedcube simulator](https://www.ryanheise.com/cube/speed.html).

For instructions on how to use or customize the keybinds, see [this video tutorial](https://youtube.com/watch?v=yRt5DVqjnEo&list=PLBQ7ltR88PRv9Rmrv7iRhupGaazEPWZi5&index=3).

For instructions on how to use piece filters, see [this video tutorial](https://youtube.com/watch?v=LAYXy5mh3FI&list=PLBQ7ltR88PRv9Rmrv7iRhupGaazEPWZi5&index=2).

## Future plans

I am currently (as of early 2026) working on Hyperspeedcube 2.0, which vastly expands the capabilities of Hyperspeedcube's puzzle engine and overhauls the UI to be more powerful and more intuitive.

### New puzzle engine

{{% status_badge "complete enough" "darkgreen" %}}

The new puzzle engine is almost completely implemented. Puzzle generators are defined using [Hyperpuzzlescript](https://github.com/HactarCE/Hyperspeedcube/tree/main/crates/hyperpuzzlescript#hyperpuzzlescript), a bespoke domain-specific programming language. Puzzle definitions support the following features:

- Puzzle generators {{% status_badge "partially complete" "yellow" %}}
- Multi-layer (hyper)planar cuts {{% status_badge "complete" "darkgreen" %}}
- Shapeshifting {{% status_badge "complete" "darkgreen" %}}
- Jumbling {{% status_badge "partially complete" "yellow" %}}
- Puzzle notation {{% status_badge "in progress" "blue" %}}
- 3- to 7-dimensional Euclidean space {{% status_badge "complete" "darkgreen" %}}
- Hot-reloading by pressing <kbd>F5</kbd> {{% status_badge "complete" "darkgreen" %}}

This is sufficient to simulate nearly every 4D+ twisty puzzle we are currently aware of and many more. Once released, Hyperspeedcube 2 will make [Magic Cube 4D](https://superliminal.com/cube/), [Magic Cube 5D](https://www.gravitation3d.com/magiccube5d/), [Magic Cube 7D](https://superliminal.com/andrey/mc7d/), [Magic Puzzle Ultimate](https://superliminal.com/andrey/mpu/), and [Magic Simplex 5D](https://superliminal.com/andrey/ms5d/) completely obsolete, and will make [pCubes](https://twistypuzzles.com/forum/viewtopic.php?t=27054) and [Magic 120 Cell](http://www.gravitation3d.com/magic120cell/index.html) largely obsolete.

See [HactarCE/Hyperspeedcube#74](https://github.com/HactarCE/Hyperspeedcube/issues/74) for a list of puzzles that will be in Hyperspeedcube 2.0.

With further modification, this new puzzle engine will also be able to support features never before seen in higher-dimensional puzzles, including certain nonplanar cuts and multiple cores (e.g., corner-turning cuboids).

I also intend to add a tiling engine, which will support everything in [MagicTile](http://roice3.org/magictile/) as well as puzzles on non-regular tilings. I'm still investigating what this would look like, and what the limits would be.

### Overhauled UI

{{% status_badge "in progress" "blue" %}}

#### Colors

{{% status_badge "complete" "darkgreen" %}}

The new color customization UI is complete. It supports built-in and user-defined color sets for each shape and a customizable global color palette.

{{% small_imgur src="Gi8Sdji.png" alt="FTO and 3x3x3, with many FTO color schemes listed on the right and a list of many colors on the left, organized into sets of various sizes, with a color picker open on one of them" %}}

#### Keybinds

{{% status_badge "in progress" "blue" %}}

The keybind sets system in Hyperspeedcube 1 is complex and unintuitive. I have plans for a system involving modes that will have just one list of keybinds organized into collapsible sections, and each section may be active in some subset of modes. Keybinds will be shared between puzzles with similar twist sets, even if the shapes are different; for example, a face-turning cube and corner-turning octahedron would share the same keybinds.

#### Piece filters

{{% status_badge "complete" "darkgreen" %}}

The new piece filters UI is complete. It is more powerful and easier to learn than the piece filters in Hyperspeedcube 1, with the following features:

- [x] Tri-state checkboxes (similar to MC7D)
- [x] Text-based filters with boolean algebra expressions
- [x] Hierarchy of piece types for big puzzles
- [x] Multiple styles for different piece sets
- [x] User-defined sequences of piece filter presets

{{% small_imgur src="YWZoATU.png" alt="14x14x14, with corners and most centers visible, but edges, wings, and a few centers hidden; on the right is a tree of piece types, each with a checkbox that is empty for visible piece types and contains an 'X' for hidden piece types" %}}
{{% small_imgur src="8Q1bB3y.png" alt="3x3x3, with some pieces completely opaque, some pieces transparent, and some pieces completely hidden; on the left is a text box and a set of checkboxes controlling the filters" %}}

While text-based filters are more expressive than the checkboxes, both systems are capable of creating the same filter views.

These features are desired for the future, but there are currently unresolved questions preventing their implementation:

- [ ] Tool to click on pieces to show/hide them
- [ ] Rotating piece filters

### Other features

There are other oft-requested features that will become even more important with the new variety of puzzles. I don't expect all of these to make it into the first release of Hyperspeedcube 2, but I intend to implement all of them eventually:

- [x] New puzzle list {{% status_badge "complete" "darkgreen" %}}
- [x] New color picker {{% status_badge "complete" "darkgreen" %}}
- [ ] Integrated timer {{% status_badge "complete" "darkgreen" %}}
- [ ] [Fewest-moves solution leaderboard](https://lb.hypercubing.xyz/?event=fmc) {{% status_badge "complete" "darkgreen" %}}
- [ ] Auto-updater {{% status_badge "partially complete" "yellow" %}}
- [ ] Timeline for analyzing speedsolves/FMC solutions
- [ ] Macros (custom move sequences)

### Following development

I'll be posting updates in the [**Hyperspeedcube 2.0 Development Updates**][hsc-updates-thread] thread in `#hyper-forum` on the {{% hypercubers_discord %}}. Once Hyperspeedcube 2.0 is ready for general use, I will ping **@everyone** in the Discord server. If you'd like to support me monetarily and get access to early builds, you can [support me on Ko-fi](https://ko-fi.com/C0C2UG3S8). Any builds I provide on Ko-fi will also be available by building from source on GitHub, and once a stable version is ready and has been beta-tested by my Ko-fi supporters, it will be available to download for everyone, for free.

{{% kofi_badge %}}

[hsc-updates-thread]: https://discord.com/channels/852389089268858922/1096955261719162910
