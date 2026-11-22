import html, os, sys

ROOT = sys.argv[1]

CARDS = [
  {
    "a": "1", "b": "2",
    "aff": {"1": "I let my creative fire burn bright.", "2": "Life knows the way, and so do I."},
    "lead": {
      "1": {
        "intro": "This is Key 1, the Gift of Freshness. There's a spark in you that's entirely your own, not borrowed or copied. It doesn't need permission to shine.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 2, the Gift of Orientation: the quiet inner compass that lets your fire move in the right direction without forcing it.",
        "q": ["What lights you up lately?", "Where does it seem to want to go?"],
      },
      "2": {
        "intro": "This is Key 2, the Gift of Orientation. You don't have to map every step. Something in you already knows the direction, even when the path isn't visible yet.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 1, the Gift of Freshness: the spark that makes the journey worth taking.",
        "q": ["Where are you trying to control the route?", "What would trusting the direction feel like?"],
      },
    },
  },
  {
    "a": "3", "b": "50",
    "aff": {"3": "I meet change with curiosity.", "50": "I stay steady at my centre."},
    "lead": {
      "3": {
        "intro": "This is Key 3, the Gift of Innovation. Change can feel like chaos, but it's often something new trying to be born. Curiosity turns it from a threat into a doorway.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 50, the Gift of Equilibrium: the still point that lets you meet change without losing yourself.",
        "q": ["What's changing around you?", "What might it be making room for?"],
      },
      "50": {
        "intro": "This is Key 50, the Gift of Equilibrium. Whatever is moving around you, there's a place inside that stays calm and fair. Coming back to it is always possible.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 3, the Gift of Innovation, a reminder that steadiness isn't standing still. It's what lets you welcome the new.",
        "q": ["Where is your centre right now?", "What helps you find your way back to it?"],
      },
    },
  },
  {
    "a": "4", "b": "49",
    "aff": {"4": "I seek to understand before I answer.", "49": "I am free to let old patterns go."},
    "lead": {
      "4": {
        "intro": "This is Key 4, the Gift of Understanding. The mind loves quick answers, but real understanding takes a breath first. It listens for the whole picture.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 49, the Gift of Revolution: what understanding makes possible, the freedom to change what no longer serves you.",
        "q": ["What question are you rushing to answer?", "What might you see if you waited a little longer?"],
      },
      "49": {
        "intro": "This is Key 49, the Gift of Revolution. Some habits, roles and relationships belonged to an earlier version of you. Letting them go isn't rejection. It's growth.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 4, the Gift of Understanding, which lets you release things with clarity rather than in a rush.",
        "q": ["Which old pattern is ready to go?", "What do you understand now that you didn't before?"],
      },
    },
  },
  {
    "a": "5", "b": "35",
    "aff": {"5": "I trust the rhythm of my life.", "35": "My life is an adventure, just as it is."},
    "lead": {
      "5": {
        "intro": "This is Key 5, the Gift of Patience. Life moves in seasons, not straight lines. What feels like waiting is often things quietly ripening.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 35, the Gift of Adventure, which finds the richness in each moment along the way.",
        "q": ["Where are you pushing, instead of pausing to see what comes to you?", "What might show up if you waited a moment before acting?"],
      },
      "35": {
        "intro": "This is Key 35, the Gift of Adventure. Adventure isn't always somewhere new. It's meeting your own life with fresh eyes and noticing what's already here.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 5, the Gift of Patience, which lets the adventure unfold in its own time.",
        "q": ["What in your life right now is quietly remarkable?", "What would change if you saw it that way?"],
      },
    },
  },
  {
    "a": "6", "b": "36",
    "aff": {"6": "I can soften without losing myself.", "36": "My heart stays open, even when life is hard."},
    "lead": {
      "6": {
        "intro": "This is Key 6, the Gift of Diplomacy. Softening isn't giving in. It's choosing warmth over winning, while still knowing where you stand.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 36, the Gift of Humanity: the open heart that makes softening possible.",
        "q": ["Where are you bracing for a fight?", "What might happen if you softened, just a little?"],
      },
      "36": {
        "intro": "This is Key 36, the Gift of Humanity. Hard times can make us close up to protect ourselves. Staying open is a quiet kind of courage, and it lets life keep reaching you.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 6, the Gift of Diplomacy, which shows you can stay open and still hold your ground.",
        "q": ["What has made you want to close up lately?", "What would help your heart feel safe enough to stay open?"],
      },
    },
  },
  {
    "a": "7", "b": "13",
    "aff": {"7": "I lead simply by being myself.", "13": "I listen deeply, to others and to me."},
    "lead": {
      "7": {
        "intro": "This is Key 7, the Gift of Guidance. You don't need a title to lead. When you live true to yourself, others quietly find their way by your example.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 13, the Gift of Discernment: the listening that makes your guidance wise.",
        "q": ["Who might be watching how you live?", "What are you showing them without saying a word?"],
      },
      "13": {
        "intro": "This is Key 13, the Gift of Discernment. Real listening means hearing what's said and what's underneath it, including your own inner voice.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 7, the Gift of Guidance: what deep listening grows into, knowing which way to go.",
        "q": ["Who in your life needs to be truly heard?", "What has your own inner voice been trying to tell you?"],
      },
    },
  },
  {
    "a": "8", "b": "14",
    "aff": {"8": "I dare to be unmistakably me.", "14": "I do what I love, and I do it well."},
    "lead": {
      "8": {
        "intro": "This is Key 8, the Gift of Style. There's no one else quite like you, and the world doesn't need a copy of anyone. Being yourself is your greatest contribution.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 14, the Gift of Competence: what happens when you put your true self into your work.",
        "q": ["Where are you trying to fit in?", "What would you do differently if you stopped?"],
      },
      "14": {
        "intro": "This is Key 14, the Gift of Competence. When you work from love rather than pressure, effort turns into flow, and the results tend to take care of themselves.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 8, the Gift of Style, a reminder that how you do it is as much yours as what you do.",
        "q": ["What do you do that makes time disappear?", "How could you make a little more room for it?"],
      },
    },
  },
  {
    "a": "9", "b": "16",
    "aff": {"9": "Every small step I take matters.", "16": "I am free to play with all my gifts."},
    "lead": {
      "9": {
        "intro": "This is Key 9, the Gift of Determination. Big changes are built from small, steady steps. Each one counts, even when you can't see the difference yet.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 16, the Gift of Versatility, which brings lightness and enjoyment to the steps along the way.",
        "q": ["What small step could you take today?", "What's one step you've already taken that you haven't given yourself credit for?"],
      },
      "16": {
        "intro": "This is Key 16, the Gift of Versatility. You don't have to choose just one thing to be good at. Your many interests and talents are meant to be enjoyed.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 9, the Gift of Determination, which helps your gifts grow through gentle, steady practice.",
        "q": ["Which of your gifts have you put aside?", "What would it feel like to play with it again?"],
      },
    },
  },
  {
    "a": "11", "b": "12",
    "aff": {"11": "I honour the dreams that light me up.", "12": "I choose my words with care and courage."},
    "lead": {
      "11": {
        "intro": "This is Key 11, the Gift of Idealism. Somewhere in you is a picture of how life could be. It isn't a fantasy to grow out of. It's a light to steer by.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 12, the Gift of Discrimination. A dream stays a dream until it's spoken. Key 12 is the voice that gives your vision shape: what to say, when, and to whom.",
        "q": ["Which dream came to mind first?", "Who would you need to say it to, and what would you say?"],
      },
      "12": {
        "intro": "This is Key 12, the Gift of Discrimination. Your words carry weight. Choosing them with care isn't holding back; it's letting what you say land where it's meant to.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 11, the Gift of Idealism. Courage needs something worth speaking for. Key 11 is the dream your words are here to serve.",
        "q": ["What have you been holding back from saying?", "What dream sits underneath it?"],
      },
    },
  },
]

e = html.escape

def journey(card, lead, other):
    L = card["lead"][lead]
    q = "<br>".join(e(x) for x in L["q"])
    return f'''  <!-- Key {lead} leads -->
  <section class="journey" id="lead-{lead}" hidden>
    <div class="step">
      <p class="label">The card that chose you</p>
      <p class="affirmation">{e(card["aff"][lead])}</p>
      <p>{e(L["intro"])}</p>
    </div>
    <div class="step">
      <p class="label">Turn the card around</p>
      <p class="affirmation">{e(card["aff"][other])}</p>
      <p>{e(L["partner"])}</p>
    </div>
    <div class="step">
      <p class="label">Sit with it</p>
      <p class="questions">{q}</p>
    </div>
  </section>
'''

def page(card):
    a, b = card["a"], card["b"]
    desc = e(card["aff"][a] + " " + card["aff"][b] + " Discover how they meet.")
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Keys {a} &amp; {b} · Phoebe Affirmations</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;1,500&family=Lato:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../style.css">
</head>
<body>
<main>

  <header class="brand">
    <div class="star">✦</div>
    <p class="name">Phoebe</p>
    <div class="tag">Affirmations</div>
  </header>

  <p class="intro">Every card holds a pair. Discover how they meet.</p>

  <p class="choose">Which one chose you?</p>
  <div class="pair">
    <button class="pick" data-lead="{a}" aria-pressed="false">
      <span class="num">KEY {a}</span>
      <span class="line">{e(card["aff"][a])}</span>
    </button>
    <button class="pick" data-lead="{b}" aria-pressed="false">
      <span class="num">KEY {b}</span>
      <span class="line">{e(card["aff"][b])}</span>
    </button>
  </div>

{journey(card, a, b)}
{journey(card, b, a)}
  <section class="meet">
    <h2>If this spoke to you</h2>
    <p>I'm Phoebe, and through Radiant Oracle I offer intuitive readings with crystals and tarot, where the card chooses you and the message unfolds through conversation. I also run group readings for events, parties and gatherings.</p>
    <div class="links">
      <a href="https://www.instagram.com/radiant.oracle/">Instagram</a>
    </div>
  </section>

  <footer>A kinder you · A brighter tomorrow</footer>

</main>
<script>
  (function () {{
    var keys = ['{a}', '{b}'];
    var picks = document.querySelectorAll('.pick');
    function show(lead, scroll) {{
      picks.forEach(function (btn) {{
        btn.setAttribute('aria-pressed', btn.dataset.lead === lead ? 'true' : 'false');
      }});
      keys.forEach(function (k) {{
        document.getElementById('lead-' + k).hidden = (k !== lead);
      }});
      if (scroll) document.getElementById('lead-' + lead).scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }}
    picks.forEach(function (btn) {{
      btn.addEventListener('click', function () {{
        history.replaceState(null, '', '#' + btn.dataset.lead);
        show(btn.dataset.lead, true);
      }});
    }});
    var start = location.hash.replace('#', '');
    if (keys.indexOf(start) !== -1) show(start, false);
  }})();
</script>
</body>
</html>
'''

import json, re

CARDS.sort(key=lambda c: int(c["a"]))

for c in CARDS:
    d = os.path.join(ROOT, "keys", f'{c["a"]}-{c["b"]}')
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w") as f:
        f.write(page(c))
    print("wrote", d)

# Home page card list (between markers)
items = "\n".join(
    f'      <p><a href="keys/{c["a"]}-{c["b"]}/">Keys {c["a"]} &amp; {c["b"]} · {e(c["aff"][c["a"]].rstrip("."))}</a></p>'
    for c in CARDS)
hp = os.path.join(ROOT, "index.html")
s = open(hp).read()
s = re.sub(r"<!-- cards:start -->.*?<!-- cards:end -->", lambda m: "<!-- cards:start -->\n" + items + "\n      <!-- cards:end -->", s, flags=re.S)
open(hp, "w").write(s)

# Draw page data
deck = [{"a": c["a"], "b": c["b"], "aff": c["aff"]} for c in CARDS]
open(os.path.join(ROOT, "draw", "deck.js"), "w").write("window.DECK = " + json.dumps(deck, ensure_ascii=False, indent=1) + ";\n")
print("deck:", len(deck), "cards")
