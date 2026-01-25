+++
date = "2026-01-25"
title = "I Do Not Use Generative AI"
+++

{{< lead >}}
And only partly because the AI industry is fucking despicable
{{< /lead >}}

<!--more-->

> Look, I know AI is controversial, but just for a moment, let's set aside our preconceived notions, our biases, the [environmental impact], the massive cost to train and run models, the [labor exploitation], the [intellectual property theft], the [inaccuracies][hallucination], the [mania it causes in users][psychosis], the [destruction of search], the [deskilling of professionals][deskilling], the devaluation of creative work, job losses, and [lack of economic value from enterprise implementations][economics].

[environmental impact]: https://www.unep.org/news-and-stories/story/ai-has-environmental-problem-heres-what-world-can-do-about
[economics]: https://www.wheresyoured.at/why-everybody-is-losing-money-on-ai/
[labor exploitation]: https://muse.jhu.edu/article/950958
[intellectual property theft]: https://jskfellows.stanford.edu/theft-is-not-fair-use-474e11f0d063
[hallucination]: https://arxiv.org/abs/2401.11817
[psychosis]: https://en.wikipedia.org/wiki/Chatbot_psychosis
[destruction of search]: https://archive.is/20250916050713/https://www.404media.co/googles-ai-is-destroying-search-the-internet-and-your-brain/
[deskilling]: https://www.media.mit.edu/publications/your-brain-on-chatgpt/

# My thoughts on generative AI

The internet doesn't need another opinion piece lambasting generative AI. As seems to be the pattern with my blog, I'm writing this so that when someone brings up the topic I can simply point them to this post and not have to say the same things over and over again.

Some claims here will go uncited. I might add citations later. I might also update this in the future to remove claims if I am shown convincing evidence to the contrary. I'm not intending to [gish gallop](https://en.wikipedia.org/wiki/Gish_gallop); I genuinely think that each one of these claims stands on its own as a reason to be skeptical, and that even one or a few of them together are sufficient to defend my viewpoint.

## Bad

### Images, video, and audio

I agree with Freya Holmér that [generative AI is a parasitic cancer](https://youtu.be/-opBifFfsMY) on creative fields.

I think that the minor novelty of typing a prompt and seeing a plausible image, video, or audio output is outweighed by the psychological and financial impact on creative hobbyists and professionals whose work the technology was trained on, and _vastly_ outweighed by the massive spread of misinformation it has enabled.

### Education

I think any extent to which generative AI has enabled "personalized learning" is vastly outweighed by enabling students to avoid developing critical thinking skills by outsourcing assignments to generative AI.

My mother taught high-school Latin for years and now teaches high-school English as a Second Language in a public school, and knows that the solutions to "improving education" are very simple:

- **Stop devaluing instructors.** Give educators the respect and pay that befits the job of educating the next generation of humanity, increasing the supply of high-quality teachers.[^teaching]
- **Improve financial inequality.** Children cannot learn when they are hungry, and parents cannot teach them to read at a young age when they do not have time to do so.
- **Do not persecute children for queerness or immigration status.** Children cannot learn when they do not feel safe.

Unfortunately none of these has a technological solution that can be sold for a profit.

[^teaching]: Several people in my life have told me that I am excellent at explaining things and would make a great teacher. I'd seriously consider that career if teachers weren't so overworked and underpaid compared to software engineers despite their jobs being vastly more important.

I've yet to hear from a single instructor that thinks generative AI even has the potential for a positive impact on education, let alone the actual effects of any of the existing offerings.

## Good

There are a handful of use cases for generative AI where I think it is clearly a net-positive, and which I would probably use myself.

### Translation

We've had machine translation via Google Translate for a long time, and they've improved with new LLM technology. I think that professional human translation should and always will be the gold standard, but professional translation is often inaccessible and so better machine translation is a net-good.

### Accessibility

Improved voice recognition, image descriptions, and speech-to-text have all massively improved computer accessibility accommodations. I think this is fantastic.

### Research

I defer to the experts doing this. Either way, generative AI is not the panacea that its marketers would like you think it is.

## Writing software

There are a number of reasons I currently do not use LLMs when writing software. They are listed here in approximate order from most to least significant.

### Environmental Impact

Generative AI uses a lot of electricity and water.

I know existing technology is manufactured unethically and unsustainably damages the environment too, and I'm not thrilled about that either, but it's pretty damn difficult to operate in the world without a laptop and a smartphone, especially as a software engineer[^other-jobs]. I at least don't want to make my environmental impact significantly worse without a damn good reason.

[^other-jobs]: There's no possible good-faith argument in favor of LLMs that includes "you should stop participating in the software industry because of its ethical/environmental impact" so I won't address here the question of whether I could realistically sustain myself doing anything else.

### Reliability

LLM output is designed to be convincing, so poor output can easily go unnoticed. [Hallucination is not a flaw that can be fixed; it is provably, mathematically inevitable.](https://arxiv.org/abs/2401.11817)

As [Rob Miles put it](https://www.youtube.com/watch?v=w65p_IIp6JY):

> The AI isn't making a mistake at all. _We_ made a mistake by expecting it to tell the truth. A language model is not "trying" to say true things. It's just trying to predict what text will come next.

I hold myself to higher standards than "code that is likely to come next." Unless I have personally reviewed every line of code produced by an LLM, I will not commit it.

### Ownership

Here's a list of the software I use the most when writing code:

| Purpose            | Tool                           | FOSS?        | Works offline? |
| ------------------ | ------------------------------ | ------------ | -------------- |
| Documentation      | rustdoc + Firefox              | ✅            | ✅              |
| Notes              | [Obsidian]                     | ❌[^obsidian] | ✅              |
| Editor             | VSCode or Zed                  | ✅            | ✅              |
| Language toolchain | `cargo`/`rustc`/`rustfmt`/etc. | ✅            | ✅              |
| Operating system   | macOS                          | ❌[^macos]    | ✅              |

I'm vaguely aware that there are local LLMs, but that they're not nearly as good as the commercial offerings which are not free [in either sense](https://en.wikipedia.org/wiki/Gratis_versus_libre) and do not work offline. I would like all of my tools to work offline, not actually because an internet connection is unreliable (although it is), but because **offline tools are much harder to take away**.

[Obsidian]: https://obsidian.md/
[^obsidian]: FOSS alternatives exist. My data is ultimately just Markdown files in a folder so I'm not necessarily stuck with Obsidian.
[^macos]: I have used Linux in the past, and would switch to it if macOS ever annoyed me enough. Currently macOS offers a slightly nicer experience for slightly less effort, and the hardware is best-in-class.

I think it is awful that there are so many professionals whose craft depends on deep knowledge and skill in a proprietary tool that has been taken away from them simply because it was no longer profitable to provide, or because they no longer had the means to afford it. I am very fortunate that in the software industry, I have the choice to avoid that fate.

### Deskilling

I already offload a lot of work to computers.

- Because I rely on Google Maps for navigation, I'm terrible at navigating my own city, even for routes I take several times a month. This is something I'd like to improve, but it's not a high priority for me.
- Because I rely on my journal for recalling recent events, I've weakened my long-term memory of what things have happened in the last week or month. I think this tradeoff is worth it because of the precision of recall my journal provides and because of the insights I can draw from so much high-quality data about my life. Crucially, my journal is entirely within my control. I could even switch to a paper medium if I had to.

Writing code requires a _lot_ of critical thinking and the thought of offloading that to a machine, _especially_ one designed with a profit motive, is extremely alarming. Even more alarming is the thought of an entire industry, or an entire _society_ doing that.

### Craftsmanship

I actually like the fiddly bits of figuring out what to name a variable, how to order fields in a struct, thinking through the logic of an algorithm. I choose libraries with excellent documentation that includes important caveats. If something is repetitive and bolierplatey, I write functions or macros or editor snippets to automate it. For one-off text transformations, I use [multiple cursors](https://zed.dev/blog/text-manipulation) (sometimes across [multiple files](https://zed.dev/docs/multibuffers)) to make a change in fewer keystrokes than it would take to describe to an LLM what I'm doing.

Why would I have a machine do something when I enjoy doing it myself?

### Productivity

Productivity is the only selling point of using LLMs for writing software. It's rather concerning, then, that studies measuring their impact on productivity often show it worsens productivity and increases bugs despite making developers _think_ that they are being more productive.

- [Using Copilot did not increase productivity, but did increase the number of bugs](https://devops.com/study-finds-no-devops-productivity-gains-from-generative-ai/) (2024)
- [Cursor with Claude 3.5/3.7 improved perceived productivity but worsened actual productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) (early 2025)

You may insist that the models have improved drastically in the last 6 months and _now_ they're ready for mainstream use, as AI evangelists have consistently claimed throughout the last 5 years. I'll believe it when I see some numbers, since clearly the "vibes" cannot be trusted.

## Frustration with the industry

So far, I have been very careful to only consider the actual uses of the technology and consequences of it being available rather than the organizations and tactics used to promote it. But I am _beyond disgusted_ with the industry that has built up around generative AI and it honestly makes feel ashamed to work in the software industry.

- Generative AI is being deployed **irresponsibly** with zero consideration for its effects on its users or society. I cannot stress enough that generative artificial intelligence is **repeatedly encouraging real people to kill others and themselves, and they are doing it**. This is fucking unconscionable.
- The tools are being pushed onto people who don't care or actively dislike it. It's **disrespectful to users**.
- Using generative AI to write software and prioritizing AI features above usability are both extensions of [**neglecting software quality**](https://tonsky.me/blog/disenchantment/) more broadly
- [Elon Musk is **illegally poisoning** the citizens of Memphis to train Grok.](https://time.com/7308925/elon-musk-memphis-ai-data-center/) For fucks sake, even if you insist on using LLMs, **do not use Grok**.
- [Electricity providers cut deals with AI companies to give them lower prices](https://www.cnbc.com/2025/11/26/ai-data-center-frenzy-is-pushing-up-your-electric-bill-heres-why.html) so folks who live in cities with AI datacenters are forced to pay **absurd electricity prices to subsidize AI usage**.
- Large corporations are operating with **complete hypocrisy around intellectual property.** I think it's absurd that they [hold onto copyright for multiple human lifespans](https://www.copyright.gov/help/faq/faq-duration.html) and defend [absurd software patents](https://en.wikipedia.org/wiki/Software_patent#Criticism), yet individuals have no power to prevent LLMs from training on and replicating their styles and works.
- The entire industry has **incredibly lax security practices**.
	- I'm sorry, people are giving LLMs **unrestricted terminal access**? _Are you out of your fucking mind??_ Just [viewing their output](https://interhumanagreement.substack.com/p/llm-output-can-take-over-your-computer) can be dangerous, let alone [running commands](https://www.da.vidbuchanan.co.uk/blog/agent-perms.html).
	- Data leaks using LLMs should not be possible because **public-facing LLMs cannot be trusted with sensitive data**.
  - And you know, run-of-the-mill [slopsquatting](https://www.theregister.com/2025/04/12/ai_code_suggestions_sabotage_supply_chain/)

> glad we're at the stage of our cyberpunk hell-timeline that we have [corporate botnets](https://jan.wildeboer.net/2025/04/Web-is-Broken-Botnet-Part-2/) [DDoSing](https://drewdevault.com/2025/03/17/2025-03-17-Stop-externalizing-your-costs-on-me.html) the [free software communities](https://www.osnews.com/story/141969/foss-infrastructure-is-under-attack-by-ai-companies/)" that they rely on, leading to [an arms race](https://thelibre.news/foss-infrastructure-is-under-attack-by-ai-companies/) between the biggest companies in the world and a [virtual anime person](https://www.twitch.tv/princessxen) developing a [proof-of-work proxy](https://anubis.techaro.lol/) with [an anime girl mascot](https://discourse.gnome.org/t/anime-girl-on-gnome-gitlab/27689) that's [now deployed by the united nations](https://xeiaso.net/notes/2025/anubis-works/)

## Would I use LLMs?

They seem genuinely useful for **quick prototyping**, but the drawbacks outweigh the benefits for me.

For **machine translation**, I'll probably keep using Google Translate. If LLMs are the most effective tool for that, then I'm sure Google Translate will integrate them. The primary drawback for this application is environmental impact, which is relatively small for translating single words or phrases (and I wouldn't trust it for translating a large text that requires a lot of context).

If I am ever unable to use my hands for an extended period of time, I would be open to **coding via voice using generative AI**. In this case I would probably treat it less like a coding assistant (as it's currently being advertised) and more like a voice-controlled keyboard that also has autocomplete and is aware of the syntactic constructs of the programming language I'm using. For example: "change the `if let` to a `match` and add a fallback that returns an anyhow error." (I'm speculating here; I haven't actually tried this workflow yet.) I could probably use a local model with lower capability, which mitigates both the "owning my tools" thing and the environment impact. If I had to use a commercial service and my livelihood depended on it, I would cope.

## Conclusion

There's some reasonable arguments in favor of them. But broadly speaking, I'm not interested in using LLMs in my workflow and a lot would have to change before I would even considering using them in the ways advocated by enthusiasts of the technology.

As for the societal impact, **fuck every tech company that is deploying AI irresponsibly**. Get your fucking shit together.
