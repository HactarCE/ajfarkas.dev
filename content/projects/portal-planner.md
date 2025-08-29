+++
title = "Portal Planner"
+++

{{< lead >}}
Advanced Nether portal planning tool for Minecraft: Java Edition
{{< /lead >}}

<a href="{{< ref `/projects/portal-planner` >}}"><img src="https://raw.githubusercontent.com/HactarCE/PortalPlanner/main/resources/icon/portalplanner.svg?sanitize=true" alt="Portal Planner logo" width="100" align="right" style="margin: 0px 0px 0px 10px"></a>

Portal Planner is a tool for planning advanced Nether portal linkages in Minecraft: Java Edition. It replicates the exact in-game computations to determine which portals are possible to link together

<!--more-->

[Try it online!](https://hactarce.github.io/PortalPlanner/)

## Download

{{< button href="https://github.com/HactarCE/PortalPlanner/releases/latest/download/portal_planner_win64.zip" >}}{{< icon "windows" >}} Windows{{< /button >}}
{{< button href="https://github.com/HactarCE/PortalPlanner/releases/latest/download/portal_planner_linux.tar.gz" >}}{{< icon "linux" >}} Linux{{< /button >}}
{{< button href="https://github.com/HactarCE/PortalPlanner/releases/latest/download/portal_planner_macos.tar.gz" >}}{{< icon "apple" >}} macOS{{< /button >}}
{{< button href="https://github.com/HactarCE/PortalPlanner/" >}}{{< icon "github" >}} Source code{{< /button >}}

## Features

- Tracks any number of portals in the <span class="blue">Overworld</span> and <span class="red">Nether</span> with custom names and colors
- 3D planar projections with arrows showing portal linkages
- Test points for precise measurement
- Customizable entity size, with teleport region shown as a white box
- Undo/redo
- Import/export to file

## Motivation

In [Minecraft](https://en.wikipedia.org/wiki/Minecraft), [Nether portals](https://minecraft.wiki/w/Nether_portal) link between corresponding points in the [Overworld](https://minecraft.wiki/w/Overworld) and the [Nether](https://minecraft.wiki/w/The_Nether) [dimensions](https://minecraft.wiki/w/Dimension) at a ratio of 8:1, such that traveling one block horizontally in the <span class="red">Nether</span> corresponds to traveling eight blocks horizontally (X or Z axis) in the <span class="blue">Overworld</span>. Vertical distance (Y axis) maps at a ratio of 1:1. For most purposes, simply multiplying or dividing coordinates by 8 is sufficient to map between the <span class="blue">Overworld</span> and <span class="red">Nether</span> to ensure that Nether portals are placed in locations that will link together.

The [exact mechanics](https://minecraft.wiki/w/Nether_portal#Portal_linkage_between_Overworld_and_Nether) of Nether portal linkage are much more complicated, however. Here is the procedure the game uses to determine where to teleport an [entity](https://minecraft.wiki/w/Entity) entering a portal:

1. The entity's X and Z coordinates[^entity-coordinates] are multiplied or divided by 8
2. These coordinates are rounded down (toward -∞) to integer block coordinates
3. The game searches for portal blocks in a <span class="blue">257x257 (Overworld)</span> or <span class="red">33x33 (Nether)</span> square prism spanning the entire height of the destination dimension, centered on those X and Z block coordinates
4. The nearest portal block (by [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance)) is selected as the teleport destination
5. The entity's coordinates are adjusted within the destination portal frame according to its position within the initial portal frame, rotated clockwise (+Z to +X) if the portals are facing perpendicular axes
6. If the entity is a projectile, its velocity vector is rotated 90 degrees (+Z to +X) if the portals are facing perpendicular axes

There are several results of these mechanics that may be surprising even to experienced Minecraft players:

- Teleportation does not always select the closest portal (due to the square prism limitation)
- The Euclidean distance prioritization may give different results for <span class="red">Nether</span>-to-<span class="blue">Overworld</span> versus <span class="blue">Overworld</span>-to-<span class="red">Nether</span> teleportation (due to the multiplication/division by 8 only applying to horizontal coordinates)
- If one portal links to another, the reverse link might not be possible, even if there are no other portals
- The destination portal depends only on the _location of the entity being teleporting_, not the location of the portal it entered
- A single portal may link to entirely different destinations depending on the exact location of the entity when teleportation occurs
- Different entities may be able to reach different destinations due to differences in hitbox size[^clipping]

These mechanics are especially useful with the new 0.1-second teleport cooldown for projectiles introduced in [version 1.21.2](https://minecraft.wiki/w/Java_Edition_1.21.2#Blocks), which enables building linkages of Nether portals that rapidly transport [ender pearls](https://minecraft.wiki/w/Ender_Pearl) from one part of the world to another. With very little infrastructure, it's possible to teleport several thousand blocks in less than a second by chaining portals across dimensions, without the player ever leaving their initial dimension. Optimizing these linkages requires knowing exactly where portals can be placed without interfering with each other. After doing this by hand in Desmos (and getting it wrong several times), I created Portal Planner.

[^entity-coordinates]: The coordinates of an entity are the exact location of the bottom center of its hitbox.
[^clipping]: Projectiles teleport instantly upon contact with a portal block, even if they contact a solid block (such as the obsidian portal frame) on the same game tick. This gives them an even wider set of possible locations, including that are outside of the portal blocks.
