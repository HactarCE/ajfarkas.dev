+++
date = "2025-04-01"
title = "Cursed Excel: “1/2”+1=45660"
canonicalUrl = "https://www.quadratichq.com/blog/cursed-excel-datetime-math"

categories = ["code"]
+++

{{< lead >}}
Learnings from trying to make an Excel-compatible spreadsheet
{{< /lead >}}

<!--more-->

_This post was [originally published on the Quadratic Blog](https://www.quadratichq.com/blog/cursed-excel-datetime-math)._

---

[Quadratic](https://www.quadratichq.com/) aspires to be the best spreadsheet for data analysis, which implies two conflicting goals:

1. Maintain feature parity with Microsoft Excel
2. Be good

I mean no offense to the authors of Excel; it is fantastic software that we at Quadratic very often hail as the gold standard of spreadsheet interaction. That said, it's reaching the ripe old age of 40 this year and its semantics seriously suffer from a decades-long accumulation of backwards-compatible cludges.

One of my favorite things about working here is that I get to reverse-engineer Excel, find strange quirks in its behavior, and decide what to do about them in Quadratic. I suffer every day so that our users may live blissfully unaware of the undocumented sins committed by Microsoft in the name of compatibility. Today you will gain a glimpse into the horrors I contend with, and then you too will live in fear of Microsoft Excel — not because you lack knowledge, but because you know too much.

## Magic numbers

For many years, geneticists have [struggled with Excel's overeager date parsing](https://en.wikipedia.org/wiki/Microsoft_Excel#Conversion_problems) applying to names like `MARCH1` or `SEPT2` that aren't meant to be dates. But Excel's date parser has much weirder edge cases.

If we type `="1/2"` into a cell, then of course it contains the text "1/2".

{{< figure
    src="jan-2.png"
    alt=`The formula bar contains ="1/2" and the selected cell contains 1/2.` >}}

What if we add 1 to that?

{{< figure
    src="jan-2-plus-1.png"
    alt=`C1 contains 1/2. D1 is selected. The formula bar contains =C1+1 and the cell contains 45660.` >}}

45660? _What??_ Here's a hint: if you try this in the future, you may get a different number.

And it's not just dates! Sometimes Excel's time parser bites off a little more than it can chew. Of course typing `10:25` into a cell results in the time <span class="yellow">10:25 a.m.</span>, but what happens if we type `10:75`?

{{< figure
    src="1075.gif"
    alt=`10:75 is typed into a cell, and it turns into 0.46875.` >}}

0.46875?? Where the heck did that come from?

I promise that I will explain what's going on here, but first we need to cover some technical documentation and some Catholic Church history.

## (Don't) read the manual

In both of these scenarios, we're tricking Excel into parsing our input as a date or time, but displaying it as a number. As the [official documentation for the `DATEVALUE()` function](https://support.microsoft.com/en-us/office/datevalue-function-04218f74-795c-4330-9191-e7ccbe0424a8) explains:

> Microsoft Excel stores dates as sequential serial numbers so they can be used in calculations. By default, <span class="green">December 31, 1899</span> is serial number `1`, and <span class="green">January 1, 2008</span> is serial number `39448` because it is 39,448 days after <span class="green">January 1, 1900</span>.

This is helpful but contains two inaccuracies. The first is that serial number `1` represents <span class="green">January 1, 1900</span>, not <span class="green">December 31, 1899</span>. In fact, Excel will never display a date before 1900 and instead insists that serial number `0` represents _<span class="green">January 0, 1900</span>_.

{{< figure
    src="jan-0-1900.png"
    alt=`The formula bar contains 1/0/1900 and the selected cell contains Saturday, January 0, 1900.` >}}

Thankfully, the mistake about serial number `1` is corrected elsewhere in [the documentation for `MONTH()`](https://support.microsoft.com/en-us/office/month-function-579a2881-199b-48b2-ab90-ddba0eba86e8) and many other functions, but there is another inaccuracy that is still present, and it is much more insidious.

{{< figure
    src="39446.png"
    alt=`A website says that there are 39446 days between 01-Jan-1900 and 01-Jan-2008.`
    href=`https://www.weeksuntil.com/daysbetween/?start-date=01-Jan-1900&end-date=01-Jan-2008` >}}

There are actually only 39,44<span class="red">6</span> days between <span class="green">January 1, 1900</span> and <span class="green">January 1, 2008</span>, not 39,44<span class="red">8</span>. I can understand an off-by-one error, but why is Excel off by 2?

Imagine I'm assigning a number to each day of the week. Monday is 1, Tuesday is 2, ..., and Friday is 5. But you wouldn't say that Friday is 5 days after Monday. It's only 4 days after, and you can calculate that by subtracting Monday's number from Friday's number: 5 - 1 = 4. The same thing is happening here: to get the number of days between <span class="green">January 1, 1900</span> and <span class="green">January 1, 2008</span>, we should really subtract the 1900 number from the 2008 number: 39448 - 1 = 3944<span class="red">7</span>. This is closer, but still off by one. To understand the remaining off-by-one error, we need to grab our time machine and travel almost 450 years into the past.

## Calendar systems

In October 1582, Pope Gregory XIII [officially decreed](https://en.wikipedia.org/wiki/Pope_Gregory_XIII#The_Gregorian_calendar) that the Catholic Church would use the new calendar system developed by [Aloysius Lilius](https://en.wikipedia.org/wiki/Aloysius_Lilius) (then deceased) and [Christopher Clavius](https://en.wikipedia.org/wiki/Christopher_Clavius). The [Julian calendar](https://en.wikipedia.org/wiki/Julian_calendar), which had a leap year every 4 years, had been in use for more than 1600 years but had caused so much drift that Easter had fallen out of alignment with the Spring equinox. The newly christened [Gregorian calendar](https://en.wikipedia.org/wiki/Gregorian_calendar) corrected the drift by adding a new rule: every year divisible by 100 is _not_ a leap year, except years divisible by 400 which _are_ still leap years. This is why the year 2000 was a leap year (because it is divisible by 400), but 1900 was not.

In 1983, almost exactly 400 years after the new calendar was adopted, Lotus Software released [Lotus 1-2-3](https://en.wikipedia.org/wiki/Lotus_1-2-3), a revolutionary spreadsheet + database + charting program. Unfortunately, news of the 1582 promulgation had not yet reached the developers of Lotus 1-2-3, so they assumed that 1900 (being a multiple of 4) was a leap year. A few years later, Microsoft released the first version of Excel with the same mistaken leap year. If you enter `Feb 28, 1900` into Excel and add one, you'll get `Feb 29, 1900` — a day that never happened, but is necessary to maintain compatibility with Lotus 1-2-3.

{{< figure
    src="feb-29-1900.png"
    alt=`C1 contains 1900-02-28. D1 is selected. The formula bar contains =C1+1 and D1 contains 1900-02-29.` >}}

This explains the other off-by-one error in the Excel documentation; Excel is counting an extra day in February 1900, so serial numbers for dates later than that are 1 larger than you'd otherwise expect.

## What happened?

Back when you still had your sanity, I promised to explain why `"1/2"+1` equals `45660` and why Excel turned `10:75` into `0.46875`.

The first one should actually make some sense once you realize that Excel is parsing `1/2` as <span class="green">January 2, 2025</span> (the year that I'm writing this). When we add 1 we get <span class="green">January 3, 2025</span>, and there were 45,6<span class="red">58</span> days between that day and <span class="green">January 1, 1900</span>. Add 2 for the reasons described earlier and we get 45,6<span class="red">60</span>, exactly what Excel says. I don't know why it displays a number instead of a date, but the number at least makes sense.

The second one requires a deep philosophical insight: _what is a time, other than a fraction of a day?_ For example, <span class="yellow">6:00 a.m.</span> is 0.25 days, so Excel represents it using the number `0.25`. By this logic, `0.46875` should represent <span class="yellow">11:15 a.m.</span>, which is 75 minutes after <span class="yellow">10:00 a.m.</span> so that's sort of like <span class="yellow">10:75 a.m.</span> if you don't think too hard about it. But deep down inside, Excel knows that this is very wrong so it displays it as a number instead.

We can even get times beyond <span class="yellow">11:59 p.m.</span> by using hours greater than 23. Typing `37:30` into a cell produces the number `1.5625`, which represents <span class="yellow">1:30 p.m.</span> _the next day_. The number `1` represents exactly <span class="yellow">midnight</span> at the beginning of <span class="green">January 1, 1900</span>, so `1.5625` represents <span class="yellow">1:30 p.m.</span> on <span class="green">January 1, 1900</span>.

## What about Google Sheets?

Google Sheets had the brilliant idea to remove <span class="green">February 29, 1900</span> by shifting the first two months of 1900 over by one, so it represents <span class="green">January 1, 1900</span> using serial number `2` instead of `1`. This is a pretty clever solution, although it's a bit awkward to start at `2` and it causes dates before <span class="green">March 1, 1900</span> to be off-by-one when importing from Excel.

## What about Quadratic?

We're building Quadratic from the ground up to work well with Python, SQL, JavaScript, and other modern programming and database tooling, so incorrect calendar systems are not an option. We use the battle-tested [chrono](https://github.com/chronotope/chrono) library for datetimes in Rust, which plays nicely with Python's built-in [datetime](https://docs.python.org/3/library/datetime.html) library and similar data types in other languages. When [importing files from Excel](https://docs.quadratichq.com/import-data/import-excel-files), we convert any cells with date formatting into the corresponding datetime. In an effort to restore balance to the universe, <span class="green">February 29, 1900</span> is converted to <span class="green">February 28, 1900</span>.

Using a [proper datetime system](https://docs.quadratichq.com/spreadsheet/date-time-formatting) has the added bonus of letting us represent dates much farther in the past than 1900, although I'd be careful with anything before 1582. Building a spreadsheet from scratch is challenging and takes a long time to get right, so if you have a use case we don't support yet, let us know on our [community forums](https://community.quadratichq.com/) or [submit a code contribution on GitHub](https://github.com/quadratichq/quadratic/)!
