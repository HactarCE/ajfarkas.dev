+++
title = "NDCell"
+++

{{< lead >}}
Multidimensional cellular automaton simulator
{{< /lead >}}

<a href="{{< ref `/projects/ndcell` >}}"><img src="https://raw.githubusercontent.com/HactarCE/NDCell/master/docs/img/ndcell_icon.svg?sanitize=true" alt="NDCell logo" width="100" align="right" style="margin: 0px 0px 0px 10px"></a>

NDCell is a work-in-progress 2D and 3D cellular automaton simulator that I will hopefully return to someday. It currently has rendering, editing, and basic simulation working, and I'm most of the way through implementing a new domain-specific cellular automaton specification language too.

<!--more-->

## Download

{{< button href="https://github.com/HactarCE/NDCell/releases/latest/download/ndcell_win64.zip" >}}{{< icon "windows" >}} Windows{{< /button >}}
{{< button href="https://github.com/HactarCE/NDCell/releases/latest/download/ndcell_linux.tar.gz" >}}{{< icon "linux" >}} Linux{{< /button >}}
{{< button href="https://github.com/HactarCE/NDCell/releases/latest/download/ndcell_macos.tar.gz" >}}{{< icon "apple" >}} macOS{{< /button >}}
{{< button href="https://github.com/HactarCE/NDCell/" >}}{{< icon "github" >}} Source code{{< /button >}}

The latest version is {{% release_badge "HactarCE/ndcell" %}}

Or see [instructions to build from source](https://github.com/HactarCE/NDCell/blob/main/BUILDING.md)

## Screenshots

<div style="display:grid; grid-template-columns: 2fr 2fr; grid-gap: 0.5rem;">
  <img src="https://i.imgur.com/vRMLNYC.png" alt="Gosper's Glider Gun simulated for 57 generations" width="384" />
  <img src="https://i.imgur.com/uKiOxqy.png" alt="Catacryst simulated for 7.9 million generations" width="384" />
  <img src="https://i.imgur.com/NAxRaYd.png" alt="WireWorld primes calculator simulated for 2.9 million generations, displaying the number 23" width="384" />
</div>
<video controls loop muted="true" poster="https://i.imgur.com/xAhILIO.jpg">
  <source src="https://i.imgur.com/xAhILIO.mp4" type="video/mp4">
</video>
