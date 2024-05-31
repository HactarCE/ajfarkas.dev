---
layout: default
title: Hyperspeedcube
permalink: /hyperspeedcube/
---

<img src="https://raw.githubusercontent.com/HactarCE/Hyperspeedcube/main/resources/icon/hyperspeedcube.svg?sanitize=true" alt="Hyperspeedcube logo" width="150" align="right">

Hyperspeedcube is a modern, beginner-friendly 3D and 4D Rubik's cube simulator with customizable mouse and keyboard controls and advanced features for speedsolving. It's been used to break numerous speedsolving records and runs on all major operating systems plus the web.

[Try it online!](https://hypercubing.xyz/hyperspeedcube/)

If you're new to hypercubing, check out [hypercubing.xyz](https://hypercubing.xyz/), the Hypercubing community website, which I also help maintain.

## Download [![Release badge]][Release link]

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/C0C2UG3S8)

[Release badge]: https://img.shields.io/github/v/release/HactarCE/Hyperspeedcube
[Release link]: https://github.com/HactarCE/Hyperspeedcube/releases/latest

Download the latest version:

- [Windows](https://github.com/HactarCE/Hyperspeedcube/releases/latest/download/hyperspeedcube_win64.zip)
- [Linux](https://github.com/HactarCE/Hyperspeedcube/releases/latest/download/hyperspeedcube_linux.tar.gz)
- [macOS](https://github.com/HactarCE/Hyperspeedcube/releases/latest/download/hyperspeedcube_macos.tar.gz)
- [source code on GitHub](https://github.com/HactarCE/Hyperspeedcube)

Or see [instructions to build from source](https://github.com/HactarCE/Hyperspeedcube/blob/main/BUILDING.md)

## Help

See [Hyperspeedcube - Troubleshooting] (https://hypercubing.xyz/software/hyperspeedcube/#troubleshooting).

## Screenshots

Click for full resolution.

{% include small_imgur.html  src="rpMgIwp.png" alt="3x3x3x3 with the far cell mid-twist" %}
{% include small_imgur.html  src="uDzvYLz.png" alt="3x3x3x3 near the end of F2L-b with many tools and settings windows open" %}
{% include small_imgur.html  src="aAVOjsD.png" alt="Solved 2x2x2" %}
{% include small_imgur.html  src="q1CFcri.png" alt="3x3x3 superflip" %}
{% include small_imgur.html  src="jWmiZIG.png" alt="3x3x3x3 with the back cell mid-twist" %}
{% include small_imgur.html  src="XAH18Lo.png" alt="Solved 3x3x3x3 with 2c pieces highlighted and stickers on the same piece connected" %}

## Features

- Supports several puzzles
  - 3D Rubik's cube from 1x1 up to 9x9
  - 4D "Rubik's hypercube" from 1x1 up to 9x9
- Import/export using `.hsc` or MC4D-compatible `.log` file
  - `.log` is available for 4D only
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

For instructions on how to use piece filters, see [this video tutorial] (https://youtube.com/watch?v=LAYXy5mh3FI&list=PLBQ7ltR88PRv9Rmrv7iRhupGaazEPWZi5&index=2).

## Future plans

I am currently (as of mid 2024) working on Hyperspeedcube 2.0, which will vastly expand the capabilities of Hyperspeedcube's puzzle engine and overhaul the UI to be more powerful and more intuitive.

### New puzzle engine

Puzzles will be defined using planar cuts, and twists will be rotations to the pieces above or below certain cuts. This is sufficient to simulate nearly every 4D+ twisty puzzle we are currently aware of and many more. This will make [Magic Cube 4D](https://superliminal.com/cube/), [Magic Cube 5D](https://www.gravitation3d.com/magiccube5d/), [Magic Cube 7D](https://superliminal.com/andrey/mc7d/), [Magic Puzzle Ultimate](https://superliminal.com/andrey/mpu/), and [Magic Simplex 5D](https://superliminal.com/andrey/ms5d/) completely obsolete, and will make [pCubes](https://twistypuzzles.com/forum/viewtopic.php?t=27054) and [Magic 120 Cell](http://www.gravitation3d.com/magic120cell/index.html) largely obsolete.

With further modification, this new puzzle engine will also be able to support features never before seen in higher-dimensional puzzles, including bandaging, jumbling, nonplanar cuts, puzzle generators (e.g., P×Q×R×S hypercuboid generator), and multiple cores (e.g., corner-turning cuboids).

I also intend to add a tiling engine, which will support everything in [MagicTile](http://roice3.org/magictile/) as well as puzzles on non-regular tilings. I'm still investigating what this would look like, and what the limits would be.

### Overhauled UI

#### Keybinds

The current keybind sets system is complex and unintuitive. I have plans for a system involving modes that will have just one list of keybinds organized into collapsible sections, and each section may be active in some subset of modes. Keybinds will be shared between puzzles with similar twist sets, even if the shapes are different; for example, a face-turning cube and corner-turning octahedron would share the same keybinds.

#### Piece filters

I plan to take inspiration from MC7D's piece filters UI to build a system that is visually simpler for beginners and more powerful for experts, using these elements:

- Tri-state checkboxes
- Hierarchy of piece types for big puzzles
- Tool to click on pieces to show/hide them
- Piece filters based on boolean algebra expressions
- Rotating piece filters

### Other features

There are other oft-requested features that will become even more important with the new variety of puzzles. I don't expect all of these to make it into the first release of Hyperspeedcube 2, but I intend to implement all of them eventually:

- New puzzle list
- New color picker
- Timer with auto splitting
- Fewest-moves solution leaderboard
- Timeline for analyzing speedsolves/FMC solutions
- Macros (custom move sequences)
- Auto-updater

### Following development

I'll be posting updates in the [**Hyperspeedcube 2.0 Development Updates**][hsc-updates-thread] thread in #hyper-forum on the {% include hypercubers_discord.html %}. Once Hyperspeedcube 2.0 is ready for general use, I will ping the **@Hyperspeedcube Update** role (and possibly **@everyone**). If you'd like to support me monetarily and get access to early builds, you can [support me on Ko-fi](https://ko-fi.com/C0C2UG3S8). Any builds I provide on Ko-fi will also be available by building from source on GitHub, and a stable version is ready and has been beta-tested by my Ko-fi supporters, it will be available to download for everyone, for free.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/C0C2UG3S8)

[hsc-updates-thread]: https://discord.com/channels/852389089268858922/1096955261719162910
