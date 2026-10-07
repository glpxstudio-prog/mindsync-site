"""Generates the service-area pages in /areas from the data below.
Run:  python3 build_areas.py   (re-run after editing any city's copy)"""
import os, html

AREAS = [
  dict(slug="orlando", city="Orlando", county="Orange County",
    intro="Orlando moves fast. Between tourism, hospitality and one of the busiest home-services markets in Florida, customers compare a handful of businesses and book whoever answers first.",
    angle="We build Orlando businesses a site that ranks locally and a follow-up system that replies in seconds, so you win the job before a competitor calls back.",
    industries=["Home services","Contractors","Restaurants","Med spas","Real estate","Event & hospitality"],
    faq=[("Do you only work with Orlando businesses?","Orlando and Central Florida are home base, so we know the market and can meet in person. We also take select clients elsewhere in Florida."),
         ("Can you help with bilingual customers?","Yes. We build English and Spanish pages and set up follow-up messages in both languages, which matters a lot across Orlando.")]),
  dict(slug="winter-park", city="Winter Park", county="Orange County",
    intro="Winter Park customers expect polish. Boutique retail, salons, wellness studios and professional firms here compete on reputation as much as price.",
    angle="We pair a refined, on-brand website with booking, reminders and an automatic review engine, so your online presence matches the experience you deliver.",
    industries=["Boutiques","Salons & spas","Wellness studios","Professional services","Interior design","Restaurants"],
    faq=[("Can the site match a premium brand?","That's the point. Design is custom to your brand, not a template, and we can coordinate photography so it looks as good as your space."),
         ("How do reviews get collected?","After an appointment or sale, customers automatically get a short text with a link to leave a Google review. You approve the wording.")]),
  dict(slug="kissimmee", city="Kissimmee", county="Osceola County",
    intro="Kissimmee runs on vacation rentals, attractions traffic and a fast-growing local population, which means lots of inquiries, often after hours and in more than one language.",
    angle="We set up instant text-back, online booking and bilingual follow-up so every inquiry gets answered, even at 11 p.m. on a Saturday.",
    industries=["Vacation rentals","Property management","Auto services","Home services","Restaurants","Tour & activity operators"],
    faq=[("What happens when I miss a call?","The caller automatically gets a text within seconds offering to help or book a time, and the lead lands in your pipeline."),
         ("Can I manage leads from my phone?","Yes. Everything (conversations, pipeline, booking) is available in a mobile app.")]),
  dict(slug="lake-mary", city="Lake Mary", county="Seminole County",
    intro="Lake Mary is a hub for corporate offices and professional services, where clients research thoroughly before they ever reach out.",
    angle="We build credibility-first websites with clear offers and lead capture that feeds a structured pipeline, so long sales cycles don't slip through the cracks.",
    industries=["Professional services","Financial & insurance","Healthcare practices","B2B services","Tech & consulting","Real estate"],
    faq=[("Does this work for B2B or longer sales cycles?","Yes. We set up pipeline stages and nurture sequences that keep you top of mind over weeks or months, not just days."),
         ("Can my team share the CRM?","Absolutely. Add team members, assign leads and see who's following up on what.")]),
  dict(slug="altamonte-springs", city="Altamonte Springs", county="Seminole County",
    intro="Altamonte Springs packs retail, medical offices and service businesses into a busy corridor, and customers have plenty of options a few minutes away.",
    angle="We help you stand out with local SEO, a fast mobile site and automated reminders that cut no-shows and keep customers coming back.",
    industries=["Medical & dental","Retail","Fitness","Auto services","Beauty","Home services"],
    faq=[("Can you reduce appointment no-shows?","Automated text and email reminders before each appointment, with easy confirm or reschedule links, make a big difference."),
         ("Do you handle Google Maps?","Yes. We set up and optimize your Google Business Profile so you show up in the local map results.")]),
  dict(slug="sanford", city="Sanford", county="Seminole County",
    intro="Sanford's historic downtown and riverfront have brought a new wave of restaurants, breweries, shops and makers, plus steady demand for trades and home services.",
    angle="We build sites that tell your story and systems that turn foot traffic and online searches into bookings, orders and repeat customers.",
    industries=["Restaurants & breweries","Shops & makers","Trades","Home services","Event venues","Real estate"],
    faq=[("We're a small team. Is this overkill?","No. The whole point is to save small teams time. Automations handle the repetitive follow-up so you don't have to."),
         ("Can you work with my existing website?","Yes. We can plug the CRM and automations into what you have, or rebuild it if it's holding you back.")]),
  dict(slug="clermont", city="Clermont", county="Lake County",
    intro="Clermont is one of the fastest-growing areas in Lake County, with new neighborhoods driving demand for contractors, fitness, and family services.",
    angle="We help Clermont businesses get found by new residents and follow up automatically, so growth turns into booked work instead of missed messages.",
    industries=["Contractors & builders","Fitness & coaching","Landscaping & pools","Family services","Real estate","Healthcare"],
    faq=[("How fast can we get set up?","Most website-plus-system builds go live in about three weeks, depending on content and approvals."),
         ("Will this help me reach new residents?","Yes. Local SEO and Google Business Profile optimization put you in front of people searching in Clermont and nearby.")]),
  dict(slug="apopka", city="Apopka", county="Orange County",
    intro="Apopka, Florida's indoor foliage capital, is home to nurseries, landscapers and a growing number of trades and family-owned businesses.",
    angle="We build simple, effective sites with quote requests that land straight in your pipeline, plus follow-ups that turn estimates into signed jobs.",
    industries=["Nurseries & growers","Landscaping","Trades","Home services","Auto services","Local retail"],
    faq=[("Can customers request a quote online?","Yes. Quote forms feed directly into your CRM and trigger an instant confirmation and follow-up sequence."),
         ("Do I need to be good with tech?","No. We set everything up, train you, and you can run it from your phone.")]),
]


SERVICES = [
  dict(slug="web-design", name="Web Design", short="Website <em>Design</em>",
    h1="Website <em>design</em> that<br>books <em>jobs</em> in",
    pitch="A fast, mobile-first website written to convert, with clear offers, strong calls to action and lead forms that drop straight into your CRM.",
    incl=["Custom design (no templates)","Conversion-focused copywriting","Mobile-first & fast loading","Lead forms connected to your CRM","English & Spanish pages","Hosting, security & updates"],
    steps=[("Discover","We learn your services, customers and what makes you different."),("Design","You review a custom design built around your brand and offers."),("Build","We write, build and connect forms, booking and tracking."),("Launch","Go live, then we monitor and improve what converts.")],
    faq=[("How long does a website take?","Most sites launch in about three weeks, depending on how quickly content and approvals come in."),("Do I own the website?","Yes. Your content and domain are yours.")]),
  dict(slug="crm", name="CRM & Pipeline", short="CRM &amp; <em>Pipeline</em>",
    h1="A <em>CRM</em> that keeps<br>every <em>deal</em> moving in",
    pitch="Every lead from your website, calls, texts, DMs and email in one place, with pipeline stages that match how you actually sell.",
    incl=["Pipeline stages built for your process","Unified inbox: SMS, email, chat, social","Lead source tracking","Deal values & forecasting","Team access & lead assignment","Mobile app"],
    steps=[("Map","We map how leads come in and how you close them today."),("Build","We set up pipelines, fields, tags and your unified inbox."),("Connect","Website, phone, calendar and social all feed the CRM."),("Train","We train you and your team and hand over a simple playbook.")],
    faq=[("I already use spreadsheets. Why switch?","A CRM shows every lead, conversation and next step in one place and triggers follow-ups automatically. Spreadsheets can’t."),("Can you import my existing contacts?","Yes. We import and organize your current list during setup.")]),
  dict(slug="automation", name="Follow-up Automation", short="Follow-up <em>Automation</em>",
    h1="Follow-up <em>on</em> autopilot<br>for <em>businesses</em> in",
    pitch="Instant replies, missed-call text-back, estimate reminders and re-engagement campaigns by SMS and email, so no lead waits and none go cold.",
    incl=["Missed-call text-back","Instant new-lead auto-replies","Estimate & quote follow-ups","Appointment reminders","Win-back & reactivation campaigns","Bilingual message templates"],
    steps=[("Audit","We find where leads are slipping today."),("Write","We write the messages in your voice, in English and Spanish."),("Automate","We build the sequences and triggers in your CRM."),("Optimize","We track replies and bookings and refine what works.")],
    faq=[("Will automated messages sound robotic?","No. We write them in your voice, and replies come straight to you so the conversation stays personal."),("Can I pause a sequence for a lead?","Yes. Any reply or stage change can stop a sequence automatically, or you can pause it manually.")]),
  dict(slug="booking-reviews", name="Booking & Reviews", short="Booking &amp; <em>Reviews</em>",
    h1="Online <em>booking</em> and<br>5-star <em>reviews</em> in",
    pitch="Let customers book themselves, get automatic reminders, and receive a review request after every job, building your reputation on repeat.",
    incl=["Online booking calendar","Text & email reminders","Confirm / reschedule links","Automatic Google review requests","Review monitoring & replies","Embeddable booking on your site"],
    steps=[("Set up","We configure your services, hours and calendar rules."),("Embed","Booking goes on your site, Google profile and social links."),("Remind","Automatic reminders cut no-shows."),("Review","Happy customers get a quick review request after each visit.")],
    faq=[("Will this reduce no-shows?","Automated reminders with easy confirm or reschedule links are one of the most effective ways to cut no-shows."),("Is asking for reviews allowed?","Yes. We send the same polite request to every customer, which follows Google’s guidelines.")]),
  dict(slug="local-seo", name="Local SEO", short="Local <em>SEO</em>",
    h1="Get <em>found</em> on Google<br><em>in</em>",
    pitch="Show up when customers search for what you do, on Google Search and in the Maps pack, with a strategy built for your city.",
    incl=["Google Business Profile optimization","On-page SEO for local keywords","Local citations & directories","City & service landing pages","Review strategy","Monthly ranking reports"],
    steps=[("Audit","We check your site, profile and competitors."),("Optimize","We fix technical issues and optimize pages and your profile."),("Build","Citations, content and reviews grow your local authority."),("Report","Monthly reports show rankings, calls and leads.")],
    faq=[("How long does SEO take?","Most businesses see early movement in 30 to 60 days, with bigger gains over 3 to 6 months."),("Are there contracts?","Standard SEO plans are month-to-month. Founding Client plans have a 6-month minimum.")]),
]

def e(x): return html.escape(x)

def head(title, desc, canon, depth):
    up = "../"*depth
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://gomindsync.com/{canon}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;800;900&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}styles.css">
</head>
<body>
<header>
  <nav class="wrap">
    <a href="{up}index.html" class="logo"><i>M</i>Mind<span>Sync</span></a>
    <div class="links" id="links">
      <a href="{up}index.html#services">Services</a>
      <a href="{up}index.html#system">The System</a>
      <a href="{up}index.html#areas">Areas</a>
      <a href="{up}index.html#pricing">Pricing</a>
      <a href="#contact">Contact</a>
    </div>
    <a href="#contact" class="btn nav-cta">Book a strategy call</a>
    <button class="burger" aria-label="Menu" onclick="document.getElementById('links').classList.toggle('open')">☰</button>
  </nav>
</header>
"""

def schema(name, a):
    return f"""<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Service","name":"{name} in {a['city']}, FL","provider":{{"@type":"ProfessionalService","name":"MindSync","url":"https://gomindsync.com","telephone":"+1-321-621-7016"}},"areaServed":{{"@type":"City","name":"{a['city']}, FL"}}}}</script>"""

def contact(a, label, hidden):
    return f"""
<section id="contact">
  <div class="wrap contact">
    <div class="info rv">
      <p class="eyebrow">Contact</p>
      <h2 style="margin-top:14px">Grow your <em>{e(a['city'])}</em> <span class="hl">business</span></h2>
      <p>Tell us about your business and we’ll reply within one business day with a free audit showing what’s leaking and how to fix it.</p>
      <a href="tel:+13216217016">(321) 621-7016</a>
      <a href="mailto:contact@mindsyncagency.com">contact@mindsyncagency.com</a>
    </div>
    <form class="rv lead-form">
      <h3>Get your free <em>{label}</em></h3>
      <input type="hidden" name="area" value="{e(a['city'])}"><input type="hidden" name="service" value="{e(hidden)}">
      <div class="row"><label>Name<input required name="name"></label><label>Phone<input type="tel" name="phone"></label></div>
      <label>Email<input type="email" required name="email"></label>
      <label>Business &amp; website<input name="business"></label>
      <label>What do you need?<textarea rows="3" name="message"></textarea></label>
      <button class="btn" type="submit">Send →</button>
      <div class="ok">Thanks! We’ll be in touch within one business day.</div>
    </form>
  </div>
</section>"""

def foot(a, up):
    return f"""
<footer>
  <div class="wrap">
    <div class="copy"><span>© <span class="yr"></span> MindSync · Serving {e(a['city'])} &amp; Central Florida</span><span><a href="{up}index.html">Home</a> · <a href="{up}index.html#areas">All areas</a></span></div>
  </div>
</footer>
<script src="{up}site.js"></script>
</body>
</html>
"""

def svc_cards(a, current=None):
    return "".join(f'<a class="area-link{" on" if s["slug"]==current else ""}" href="{s["slug"]}.html">{s["short"]} <span>→</span></a>' for s in SERVICES if s["slug"]!=current)

def hub(a):
    others = [o for o in AREAS if o["slug"] != a["slug"]]
    chips = "".join(f"<li>{e(i)}</li>" for i in a["industries"])
    faqs = "".join(f"<details><summary>{e(q)}</summary><p>{e(x)}</p></details>" for q,x in a["faq"])
    near = "".join(f'<a class="area-link" href="../{o["slug"]}/index.html">{e(o["city"])} <span>→</span></a>' for o in others)
    svcs = "".join(f'<a class="svc-card rv" href="{s["slug"]}.html"><span class="no">0{i+1}</span><h3>{s["short"]}</h3><p>{e(s["pitch"])}</p><b>Learn more →</b></a>' for i,s in enumerate(SERVICES))
    return head(f"Websites &amp; Sales Systems in {e(a['city'])}, FL | MindSync",
        f"MindSync builds websites with CRM, follow-up automation, booking and local SEO for {e(a['city'])}, FL businesses.",
        f"areas/{a['slug']}/", 2) + schema("Websites & sales systems", a) + f"""
<section class="hero area-hero">
  <div class="wrap">
    <p class="eyebrow rv"><a href="../../index.html#areas">Areas we serve</a> · {e(a['city'])}, FL · {e(a['county'])}</p>
    <h1 class="rv" style="margin-top:22px">Websites <em>that</em> close<br>deals <em>in</em> <span class="hl">{e(a['city'])}.</span></h1>
    <p class="lead rv">{e(a['intro'])}</p>
    <div class="ctas rv"><a href="#contact" class="btn">Get a free {e(a['city'])} growth audit →</a><a href="#services" class="btn alt">Explore services</a></div>
  </div>
</section>
<section>
  <div class="wrap intro">
    <div class="rv"><p class="eyebrow">Built for {e(a['city'])}</p><h2 style="margin-top:16px">More <em>leads</em> answered. More <span class="hl">deals</span> closed.</h2></div>
    <div class="rv"><p>{e(a['angle'])}</p><p>Everything runs from one place: website, inbox, pipeline, calendar and reviews, in English or Spanish.</p></div>
  </div>
</section>
<section class="band" id="services">
  <div class="wrap">
    <div class="center"><p class="eyebrow rv">Services in {e(a['city'])}</p><h2 class="rv" style="margin-top:14px">Pick a <em>piece</em> or get the <em>whole system</em></h2></div>
    <div class="svc-cards">{svcs}</div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="svc-head rv"><div><p class="eyebrow">Who we help</p><h2 style="margin-top:14px">{e(a['city'])} <em>businesses</em> we build for</h2></div><p>If customers search for you, call you or request quotes, the system works for you.</p></div>
    <ul class="chips rv">{chips}</ul>
  </div>
</section>
<section class="band">
  <div class="wrap center">
    <p class="eyebrow rv">FAQ</p><h2 class="rv" style="margin-top:14px">{e(a['city'])} <em>questions</em></h2>
    <div class="faq-box rv">{faqs}<details><summary>How much does it cost?</summary><p>Founding Client rate: $500 setup + $100/mo for the first 5 businesses (6-month minimum, text &amp; email usage billed at cost). Standard plans start at $2,500 setup + $297/mo.</p></details></div>
  </div>
</section>""" + contact(a, "audit", "All services") + f"""
<section><div class="wrap"><p class="eyebrow rv">Nearby areas</p><h2 class="rv" style="margin:14px 0 36px">Also <em>serving</em></h2><div class="area-grid rv">{near}</div></div></section>""" + foot(a, "../../")

def service_page(a, s):
    incl = "".join(f"<li>{e(x)}</li>" for x in s["incl"])
    steps = "".join(f'<div class="step rv"><div class="ic">{i+1}</div><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i,(t,d) in enumerate(s["steps"]))
    faqs = "".join(f"<details><summary>{e(q)}</summary><p>{e(x)}</p></details>" for q,x in s["faq"])
    chips = "".join(f"<li>{e(i)}</li>" for i in a["industries"])
    others = [o for o in AREAS if o["slug"] != a["slug"]]
    near = "".join(f'<a class="area-link" href="../{o["slug"]}/{s["slug"]}.html">{s["name"]} in {e(o["city"])} <span>→</span></a>' for o in others)
    title = f"{s['name']} in {a['city']}, FL | MindSync"
    return head(e(title), f"{e(s['name'])} for {e(a['city'])}, FL businesses. {e(s['pitch'])}", f"areas/{a['slug']}/{s['slug']}.html", 2) + schema(s["name"], a) + f"""
<section class="hero area-hero">
  <div class="wrap">
    <p class="eyebrow rv"><a href="../../index.html#areas">Areas</a> · <a href="index.html">{e(a['city'])}, FL</a> · {e(s['name'])}</p>
    <h1 class="rv" style="margin-top:22px">{s['h1']} <span class="hl">{e(a['city'])}.</span></h1>
    <p class="lead rv">{e(s['pitch'])}</p>
    <div class="ctas rv"><a href="#contact" class="btn">Get a free {e(s['name'].lower())} audit →</a><a href="tel:+13216217016" class="btn alt">(321) 621-7016</a></div>
  </div>
</section>
<section>
  <div class="wrap intro">
    <div class="rv"><p class="eyebrow">{e(s['name'])} · {e(a['city'])}</p><h2 style="margin-top:16px">Why it <em>matters</em> in <span class="hl">{e(a['city'])}</span></h2></div>
    <div class="rv"><p>{e(a['intro'])}</p><p>{e(a['angle'])}</p></div>
  </div>
</section>
<section class="band">
  <div class="wrap">
    <div class="svc-head rv"><div><p class="eyebrow">What’s included</p><h2 style="margin-top:14px">{s['short']} <em>for</em> {e(a['city'])}</h2></div><p>Built to plug into the rest of the MindSync system whenever you’re ready.</p></div>
    <ul class="incl rv">{incl}</ul>
  </div>
</section>
<section class="sys">
  <div class="wrap">
    <p class="eyebrow rv">How it works</p>
    <h2 class="rv" style="margin-top:14px;max-width:820px">Simple <em>process</em>, real <em>results</em>.</h2>
    <div class="flow four">{steps}</div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="svc-head rv"><div><p class="eyebrow">Who it’s for</p><h2 style="margin-top:14px">{e(a['city'])} <em>businesses</em> we help</h2></div></div>
    <ul class="chips rv">{chips}</ul>
  </div>
</section>
<section class="band">
  <div class="wrap center">
    <p class="eyebrow rv">FAQ</p><h2 class="rv" style="margin-top:14px">{e(s['name'])} <em>questions</em></h2>
    <div class="faq-box rv">{faqs}{"".join(f"<details><summary>{e(q)}</summary><p>{e(x)}</p></details>" for q,x in a['faq'][:1])}</div>
  </div>
</section>""" + contact(a, "audit", s["name"]) + f"""
<section><div class="wrap">
  <p class="eyebrow rv">More in {e(a['city'])}</p><h2 class="rv" style="margin:14px 0 36px">Other <em>services</em></h2>
  <div class="area-grid rv">{svc_cards(a, s['slug'])}</div>
  <p class="eyebrow rv" style="margin-top:60px">{e(s['name'])} nearby</p>
  <div class="area-grid rv" style="margin-top:20px">{near}</div>
</div></section>""" + foot(a, "../../")

import shutil
shutil.rmtree("areas", ignore_errors=True)
count=0
for a in AREAS:
    os.makedirs(f"areas/{a['slug']}", exist_ok=True)
    open(f"areas/{a['slug']}/index.html","w").write(hub(a)); count+=1
    for s_ in SERVICES:
        open(f"areas/{a['slug']}/{s_['slug']}.html","w").write(service_page(a, s_)); count+=1

# homepage areas block + sitemap
cards = "".join(f'<div class="area-card rv"><a class="city" href="areas/{a["slug"]}/index.html">{html.escape(a["city"])} <span>→</span></a><div class="svc-links">' + " ".join(f'<a href="areas/{a["slug"]}/{s_["slug"]}.html">{s_["name"]}</a>' for s_ in SERVICES) + '</div></div>' for a in AREAS)
open("_area_cards.html","w").write(cards)
urls = ["https://gomindsync.com/"] + [f"https://gomindsync.com/areas/{a['slug']}/" for a in AREAS] + [f"https://gomindsync.com/areas/{a['slug']}/{s_['slug']}.html" for a in AREAS for s_ in SERVICES]
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
print("built", count, "pages")
