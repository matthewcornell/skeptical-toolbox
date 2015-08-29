# Proposal: An online skeptical toolbox.

I propose a web application that, given a URL of a news story, blog, or other piece of writing on any topic, runs a set of concerted thinking tools that present information useful to determining the truth of the piece. The user engages with some or all the tools to decide how trustworthy she believes the writing to be. In one sense, the tool is like a critical thinking 'gopher' that supports users as curious investigators of information, e.g., an unbiased meta information dashboard.

Note: This quasi-mixed initiative approach is an intermediate step until actual automated fact-checking can be done, which is still a research topic, e.g., [Knowledge-Based Trust: Estimating the Trustworthiness of Web Sources](http://arxiv.org/pdf/1502.03519v1.pdf). This project does no deep analysis of content, such as argumentation recognition, sentiment analysis, or any factual content. Instead it extracts useful information and links that are presented to the user for her ultimate analysis: reasoned judgement.


# Motivation

The goal is to engage people in a kind of stealth critical thinking and get them to start questioning the information they let into their lives (damping the echo chamber, if you will). A related problem is that, "far too often, journalists who lack a background in science simply repeat what a press release claims to be true, or quote from someone else’s article without checking into its veracity." (From [How To Be a Skeptical News Consumer](http://www.skeptic.com/eskeptic/13-06-12/).)

# Audience

Our audience is curious and intellectually honest readers who are willing to challenge their own beliefs while they investigate a piece of writing's trustworthiness. They will be answering questions for themselves such as:

* What is my opinion about this issue?
* What do you disagree with?
* Who mentioned do you trust?


# Development philosophy

We are shooting for an 80/20 payoff: What relatively simple techniques can we use to get very helpful results?


# The tools

The tools that the application brings to bear are fairly standard critical thinking ones, with [Online Tools for Skeptical Fact Checking](http://www.csicop.org/specialarticles/show/online_tools_for_skeptical_fact_checking) providing an excellent summary. Below we list the particular tools in mind (see skeptical-toolbox.xmind for an [XMind](http://www.xmind.net/) file giving details - still a bit rough, though). Note that this is a preliminary list that needs tighter thinking.

* URL analysis
* link analysis (outgoing, incoming)
* freshness measure (date of publication)
* fake news detector (hoaxes)
* extracted entity and topic links (people, topics)
* originality checks (following the trail of the information)
* check against fact-checking sites (e.g., [FactCheck.org](http://www.factcheck.org/), [Snopes.com](http://snopes.com/), [skepticalscience.com](http://skepticalscience.com/))
* check against reference sites (general as well as domain-specific, e.g., [The Skeptic's Dictionary](http://www.skepdic.com/)
* verify people
* verify quotes
* check sources


If possible:
* a simple controversy indicator?
* a simple meme tracker?


# Implementation

Fortunately the tools cover a range of complexity, which affords our quickly rolling out something useful using the simpler ones, and progressively introduce more sophisticated tools as the toolbox develops. Some of the resources we have in mind to mine are:

* [Wikipedia](https://www.wikipedia.org/) (entities, topics)
* [Google News](https://news.google.com/) (trends)
* Web search (mentions, duplicates)
* [Google Trends](https://www.google.com/trends/)
* Knowledge- and data-bases like [Freebase](http://www.freebase.com/) and [DBpedia](http://wiki.dbpedia.org/).


# Future: An automated guide

If the project appears useful, we envision adding a meta layer: an interactive wizard that guides users through using the tools via standard [critical thinking](https://en.wikibooks.org/wiki/A-level_Critical_Thinking) pedagogy, such as assessing a source's credibility:

1. Neutrality – How impartial a source of information is (biased or not).
2. Vested Interest – When a person or organisation have something to gain from supporting a point of view.
3. Expertise – Where the writer of information has specialist subject knowledge in a particular area.
4. Reputation – The regard in which a person of organisation is held in, based on their track record and their status.
5. Observation – A report from someone who directly perceived (heard, saw, felt) an event – an eyewitness account.
6. Circumstantial evidence - Physical evidence supporting the conclusion.
7. Corroboration – Where more than one source of evidence supports the same conclusion.
8. Selectivity – A measure of how representative information is compared with all of the information available.
9. Context – The situation in which information is collected.
