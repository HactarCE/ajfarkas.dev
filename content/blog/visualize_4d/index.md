+++
date = "2024-11-24"
title = "Is It Possible To Visualize 4D?"

categories = ["math", "puzzles"]
+++

{{< lead >}}
Yes, and you can learn it by practicing, just like any other skill
{{< /lead >}}

<!--more-->

_This post is about [4 spatial dimensions](https://en.wikipedia.org/wiki/Four-dimensional_space), not [4D spacetime](https://en.wikipedia.org/wiki/Spacetime)._

---

> Is it possible for humans to understand <span class="magenta">4-dimensional</span> geometry?

> Is it possible for humans to visualize <span class="magenta">4 spatial dimensions</span>?

I see these questions a lot in geometry and [hypercubing] circles. A common response, which I believed for many years, is this:

> No, it's impossible for humans to visualize <span class="magenta">4D</span> because we are <span class="green">3D</span> creatures with <span class="green">3D</span> brains.

Or worse:

> Our eyes are <span class="green">3D</span> so we cannot ever truly see in <span class="magenta">4D</span>.

**<span class="red">These answers is utterly unhelpful and mostly wrong.</span>**

My answers are in the [conclusion](#conclusion). The rest of this post is a deep dive into the semantics of those two questions, and answering them both using observable facts about human perception and capabilities.

## What's wrong with those answers?

- Our computers are <span class="green">3D</span>, yet they can perform <span class="magenta">4D</span> computations. Given enough time and scratch paper, humans are able to perform any computation a computer can.
- Our retinas are <span class="yellow">2D</span>[^depth], yet we apparently visualize <span class="green">3D</span>.
- Blind people are able to operate in <span class="green">3D</span> environments, so vision is not necessary for many <span class="green">3D</span> reasoning tasks.

[^depth]: Humans are able to [estimate depth](https://en.wikipedia.org/wiki/Depth_perception) using both **binocular** (2 eyes) and **monocular** (1 eye) techniques. You could argue that binocular vision constitutes "<span class="green">3D</span> vision," but binocular vision is obviously not <span class="green">3D</span> in the same way that monocular vision is <span class="yellow">2D</span>. Besides, humans are able to navigate <span class="green">3D</span> environments quite well with one eye closed or when they are simulated and displayed on a computer screen, so while binocular vision is useful when discussing the _practicalities_ of <span class="magenta">4D</span> visualization and reasoning, it is irrelevant when discussing the _possibilities_.

## Take it down a notch

When asking a question about higher dimensions, a very useful tool is **dimensional analogy**. Pondering the same question in a lower dimension [does not always](https://en.wikipedia.org/wiki/Rotations_in_4-dimensional_Euclidean_space) give the right answer, but it almost always yields insights that do apply in higher dimensions. We'll break down these questions into smaller ones and use dimensional analogy to help us answer them.

## Can humans understand <span class="magenta">4D</span> geometry? {#understand}

First, what does it mean to "understand <span class="green">3D</span> geometry"? The [Wikipedia page for "spatial ability"](https://en.wikipedia.org/wiki/Spatial_ability) lists many distinct tasks, which we'll analyze one at a time.

### Spatial perception

Humans are generally able to take in sensory perceptual information (typically visual, but sometimes tactile, [proprioceptive], or [echolocational]) to build a mental model of a <span class="green">3D</span> environment and objects relative to their own position. This same skill applies in <span class="green">3D</span> video games.

[echolocational]: https://en.wikipedia.org/wiki/Human_echolocation
[proprioceptive]: https://en.wikipedia.org/wiki/Proprioception

Anyone who has played [<span class="magenta">4D</span> Miner](https://store.steampowered.com/app/1941640/4D_Miner/) or [<span class="magenta">4D</span> Golf](https://store.steampowered.com/app/2147950/4D_Golf/) a sufficient amount can attest that it is possible to build a mental model of a (virtual) <span class="magenta">4D</span> environment and objects relative to their own position. <span class="magenta">4D</span> Miner displays a <span class="green">3D</span> [cross-section] of the space, while <span class="magenta">4D</span> Golf uses a cross-section with an optional [orthographic projection] overlay. Both games allow free <span class="magenta">4D</span> rotation with the constraint that the vertical axis remains fixed.

#### <span class="magenta">4D</span> Blocks

> Oh, and by the way, the cute little trains are now truly <span class="magenta">four-dimensional</span> [...]. The train moves and is indescribably cute, and you can make it go forward and backward and control all the track switches.

I would be remiss if I did not mention [<span class="magenta">4D</span> Blocks](https://www.urticator.net/blocks/) by John McIntosh. It is much older and less well-known than the more mainstream <span class="magenta">4D</span> games, but is notable for using a [wireframe] [perspective projection] with no cross-section view. While <span class="green">3D</span> cross-sections are easier for humans to parse using existing <span class="green">3D</span> visual processing, they limit how much of an environment or object can be perceived at once and make [mental rotation](#specific-tasks) more difficult.

[wireframe]: https://en.wikipedia.org/wiki/Wire-frame_model

{{< figure
    src="4d_blocks.png"
    alt=`Left: 3D-to-2D perspective projection of orange rails leading into the distance, then turning left. Right: 4D-to-3D perspective projection of orange rails leading into the distance, then turning left.`
    caption=`
On the left is a <span class="green">3D</span> scene, perspective-projected to a <span class="yellow">2D</span> square. On the right is a <span class="magenta">4D</span> scene, perspective-projected to a <span class="green">3D</span> cube (which is then orthographic-projected to the <span class="yellow">2D</span> screen). In both scenes, an orange railroad track extends forwards from below the current position, then turn left. As the rails lead farther away, they become smaller and recede to the center of the projection.` >}}

This is much more difficult to understand at first than cross-sections, but is arguably more powerful. After spending some time in the program, the visualization starts to become intuitive---smaller objects near the center of the projection are farther away, and moving forward causes far-away objects in front to become closer, making them appear to grow.

<span class="magenta">4D</span> Blocks and its predecessor, [<span class="magenta">4D</span> Maze](https://www.urticator.net/maze/), are the only <span class="magenta">4D</span> games I'm aware of with first-person camera controls and an unconstrained vertical axis. Unfortunately they have no mouse controls and the keyboard controls are not particularly satisfying to use. I would love to see a modern rewrite[^blocks-rewrite].

[^blocks-rewrite]: Luna Harran [started one](https://github.com/Sonicpineapple/Blocks), but it's currently stalled because 4D occlusion is challenging.

### Spatial visualization

"Spatial visualization" seems to be defined rather vaguely in different places. As I'm writing this, Wikipedia says this [in one place](https://en.wikipedia.org/wiki/Spatial_ability#Spatial_visualization):

> **Spatial visualization** is characterized as complicated multi-step manipulations of spatially presented information.

And this [in another](https://en.wikipedia.org/wiki/Spatial_visualization_ability):

> **Spatial visualization ability** or **visual-spatial ability** is the ability to mentally manipulate 2-dimensional and 3-dimensional figures. It is typically measured with simple cognitive tests and is predictive of user performance with some kinds of user interfaces.

I think [hypercubing][hypercubing][^5d-twisty] and playing [<span class="magenta">4D</span> Sokoban](https://coreyhardt.itch.io/4d) qualify for both of these definitions, and humans are certainly capable of both.

[^5d-twisty]: You could argue that solving a <span class="magenta">4D</span> Rubik's Cube only requires reasoning about spherical <span class="green">3D</span> space and therefore does not count. If that's the case, then imagine I'm talking about a <span class="blue">5D</span> Rubik's cube instead, which lives in spherical <span class="magenta">4D</span> space.

Neither of these definitions mentions the subjective experience of visualizing something in the mind's eye, but we'll address that in [Can humans visualize <span class="magenta">4D</span> geometry?](#visualize).

### Specific tasks

**Mental rotation**, **mental animation**, and **spatial working memory** in higher dimensions are all used extensively in [hypercubing]:

- We use **mental animation** to predict where a piece will appear after doing some sequence of moves.
- We use **mental rotation** to compose the rotations that will be applied to a piece and predict whether it will match the surrounding pieces.
- We use **spatial working memory** to track which areas of the puzzle are solved and where we have placed partially-solved blocks of pieces.

Learning hypercubing is essentially the process of training these three skills in <span class="magenta">4D</span> and higher, and applying them using [a handful of general techniques](https://hypercubing.xyz/techniques/). This is true for solving <span class="green">3D</span> twisty puzzles as well, except for stages that are particularly [algorithmic](https://www.speedsolving.com/wiki/index.php/Algorithm) (such as the last layer in most <span class="green">3D</span> Rubik's cube methods).

Wikipedia also lists **mental folding** (the ability to fold a <span class="yellow">2D</span> shape into a <span class="green">3D</span> solid) and **visual penetrative ability** (the ability to predict what the inside of something will look like based on external characteristics). While it's very common to see <span class="magenta">4D</span> shapes described using their <span class="green">3D</span> nets, I haven't seen any case of someone deducing properties of the <span class="magenta">4D</span> shape that aren't obvious from the net. I'll write off these two as "probably possible given some practice, but no one's done it."

## Can humans visualize <span class="magenta">4D</span> geometry? {#visualize}

Visualizing anything in your mind depends on two factors:

1. Are you [aphantasic](https://en.wikipedia.org/wiki/Aphantasia), [hyperphantasic](https://en.wikipedia.org/wiki/Hyperphantasia), or phantasia-typical?
2. Do you have a sufficient mental model of the thing to predict how it looks?

If someone is not aphantasic[^aphantasia], and they have enough understanding of <span class="green">3D</span> geometry to predict what a <span class="green">3D</span> environment or object will look like, then they should be able to visualize <span class="green">3D</span> geometry with no issues.

[^aphantasia]: I am aphantasic, so I have no mental imagery. People are sometimes surprised that this doesn't pose a challenge for me in spatial reasoning tasks. I am unable to _visualize_ anything in my mind, but I am perfectly capable of _conceptualizing the appearance of_ things. Aphantasics like myself often use these terms interchangeably, perhaps not even realizing that they are different. For non-aphantasics, visualizing something depends only on the ability to conceptualize its appearance, so there is no difference in _capability_ between the two tasks. Besides this brief mention of aphantasia, the distinction doesn't matter in this article, so most of the time I use "visualize" as a shorthand for "conceptualize the appearance of."

Similarly, if someone is not aphantasic, and they have [enough understanding](#understand) of <span class="magenta">4D</span> geometry to predict what a <span class="magenta">4D</span> environment or object will look like, then they should be able to visualize <span class="magenta">4D</span> geometry with no issues.

The question then remains: what does a <span class="magenta">4D</span> object look like? Let's use dimensional analogy for that as well.

### What does a <span class="green">3D</span> object look like? {#what-does-a-3d-object-look-like}

When you look at a <span class="green">3D</span> object in the world, in a book, or on a computer screen, you see a <span class="yellow">2D</span> [projection] of it. That's what it looks like.

{{< figure
    src="magritte_pipe.jpg"
    alt=`Magritte's "La Trahison des Images" ("The Treachery of Images") (1928-9) or "Ceci n'est pas une pipe" ("This is not a pipe"). Sometimes translated as "The Betrayal of Images" By René Magritte, 1898-1967. Public Domain in the United States via Wikipedia.`
    caption=`This is not a pipe. It's a <span class="yellow">2D</span> projection of one.`
    href="https://en.wikipedia.org/wiki/The_Treachery_of_Images" >}}

If some hypothetical <span class="magenta">4D</span> creature with a <span class="green">3D</span> retina were to look at a <span class="green">3D</span> object, they would instead see a <span class="green">3D</span> [perspective distortion](https://en.wikipedia.org/wiki/Perspective_distortion) of it. But we are not <span class="magenta">4D</span> creatures, so to us it looks like its <span class="yellow">2D</span> [projection].

### What does a <span class="magenta">4D</span> object look like? {#what-does-a-4d-object-look-like}

When you look at a <span class="magenta">4D</span> object in a book or on a computer screen, you see a <span class="yellow">2D</span> projection of some <span class="green">3D</span> representation of the thing (typically either a [perspective projection] or a <span class="green">3D</span> [cross-section], or perhaps multiple <span class="green">3D</span> cross-sections).

{{< figure
    src="magritte_hypercube.png"
    alt=`Projection of a hypercube, overlaid on a parchment background, with the caption "Ceci n'est pas une hypercube." Hypercube image (inverted) by Jason Hise, Public Domain via Wikipedia. I hereby publish this image is the Public Domain.`
    caption=`This is not a hypercube. It's a <span class="yellow">2D</span> projection of one.` >}}

If some hypothetical <span class="magenta">4D</span> creature with a <span class="green">3D</span> retina were to look at a <span class="magenta">4D</span> object, they would instead see a <span class="green">3D</span> [perspective projection] of it. But we are not <span class="magenta">4D</span> creatures, so to us it looks like its <span class="yellow">2D</span> [projection].

### But <span class="magenta">4D</span> objects don't exist! {#4d-objects-dont-exist}

Neither do unicorns, yet if I show you a picture of a unicorn and ask what you see you'll tell me you see a unicorn.

It's useful to talk about things that do not exist in the real world as though they do. One of the most powerful capabilities of human thought is the ability to work with _representations of an object_ rather than _the object itself_. You may insist on distinguishing between an object and its visual representations, but this is [actively unhelpful](https://en.wikipedia.org/wiki/Cooperative_principle) most of the time.

### But we only have <span class="yellow">2D</span> vision! {#2d-vision}

This is true, so it's quite difficult (perhaps impossible!) to imagine the sensation of <span class="green">3D</span> vision. <span class="green">3D</span> visual perception would be helpful for visualizing <span class="magenta">4D</span> space and <span class="magenta">4D</span> objects, but it is not necessary. <span class="green">3D</span> vision would also be helpful for visualizing <span class="green">3D</span> geometry, yet we make do without it.

## Conclusion

There is ample evidence to conclude that it is entirely possible for humans to understand and visualize <span class="magenta">4D</span> space, despite being <span class="green">3D</span> creatures with <span class="yellow">2D</span> vision. Puzzles and video games in <span class="magenta">4D</span> space require all manner of high-dimensional spatial reasoning skills and are enjoyed by a wide audience. There is typically a learning curve, but high-dimensional spatial reasoning is a skill that can be acquired and practiced like any other.

So please, stop saying it's impossible.

[hypercubing]: https://hypercubing.xyz/
[cross-section]: https://en.wikipedia.org/wiki/Cross_section_(geometry)
[orthographic projection]: https://en.wikipedia.org/wiki/Orthographic_projection
[perspective projection]: https://en.wikipedia.org/wiki/Perspective_(graphical)
[projection]: https://en.wikipedia.org/wiki/3D_projection
