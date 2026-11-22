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
        "try": "Place a hand just below your ribs and breathe into it. Imagine a small warm flame there, growing a little brighter with each breath in. Notice what it wants to light up.",
        "q": ["What lights you up lately?", "Where does it seem to want to go?"],
      },
      "2": {
        "intro": "This is Key 2, the Gift of Orientation. You don't have to map every step. Something in you already knows the direction, even when the path isn't visible yet.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 1, the Gift of Freshness: the spark that makes the journey worth taking.",
        "try": "Close your eyes and let your body sway very slightly, side to side, until it finds its own still centre. Rest there. Notice the quiet sense of which way feels right.",
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
        "try": "Think of something that's changing. Instead of tensing, raise your eyebrows slightly, as if you're curious, and breathe out. Ask yourself, \"I wonder what this could become?\"",
        "q": ["What's changing around you?", "What might it be making room for?"],
      },
      "50": {
        "intro": "This is Key 50, the Gift of Equilibrium. Whatever is moving around you, there's a place inside that stays calm and fair. Coming back to it is always possible.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 3, the Gift of Innovation, a reminder that steadiness isn't standing still. It's what lets you welcome the new.",
        "try": "Sit tall and place both hands on your lower belly. Breathe slowly in for four, out for six, three times. Feel the steady place that stays calm underneath everything.",
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
        "try": "Before answering anything today, try one slow breath first. Practise now: think of a question on your mind, breathe in and out slowly, and notice what arrives in the pause.",
        "q": ["What question are you rushing to answer?", "What might you see if you waited a little longer?"],
      },
      "49": {
        "intro": "This is Key 49, the Gift of Revolution. Some habits, roles and relationships belonged to an earlier version of you. Letting them go isn't rejection. It's growth.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 4, the Gift of Understanding, which lets you release things with clarity rather than in a rush.",
        "try": "Make a loose fist, as if you're holding on to an old habit. Breathe in. As you breathe out, slowly open your hand. Notice how it feels to let go.",
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
        "try": "Place a hand on your chest and feel your heartbeat or breath for a few moments. Let it set the pace. There's nowhere to rush to right now.",
        "q": ["Where are you pushing, instead of pausing to see what comes to you?", "What might show up if you waited a moment before acting?"],
      },
      "35": {
        "intro": "This is Key 35, the Gift of Adventure. Adventure isn't always somewhere new. It's meeting your own life with fresh eyes and noticing what's already here.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 5, the Gift of Patience, which lets the adventure unfold in its own time.",
        "try": "Look around you as if you've just arrived somewhere new for the very first time. Find one thing you've never really noticed before.",
        "q": ["What in your life right now is quietly remarkable?", "What would change if you saw it that way?"],
      },
    },
  },
  {
    "a": "6", "b": "36",
    "aff": {"6": "I soften and stay true to myself.", "36": "My heart stays open, even when life is hard."},
    "lead": {
      "6": {
        "intro": "This is Key 6, the Gift of Diplomacy. Softening isn't giving in. It's choosing warmth over winning, while still knowing where you stand.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 36, the Gift of Humanity: the open heart that makes softening possible.",
        "try": "Notice where you're holding tension: jaw, shoulders, hands. Breathe into that place and let it soften by just ten percent. Notice that you're still you.",
        "q": ["Where are you bracing for a fight?", "What might happen if you softened, just a little?"],
      },
      "36": {
        "intro": "This is Key 36, the Gift of Humanity. Hard times can make us close up to protect ourselves. Staying open is a quiet kind of courage, and it lets life keep reaching you.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 6, the Gift of Diplomacy, which shows you can stay open and still hold your ground.",
        "try": "Place a hand on your heart and breathe gently into it. Imagine it softening and widening a little with each breath, like a door easing open.",
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
        "try": "Stand or sit tall, chin level, shoulders relaxed. Take a breath and feel what it's like to simply take up your own space.",
        "q": ["Who might be watching how you live?", "What are you showing them without saying a word?"],
      },
      "13": {
        "intro": "This is Key 13, the Gift of Discernment. Real listening means hearing what's said and what's underneath it, including your own inner voice.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 7, the Gift of Guidance: what deep listening grows into, knowing which way to go.",
        "try": "Close your eyes and listen to the furthest sound you can hear, then the nearest, then the sound of your own breath. Ask yourself quietly, \"What do I need to hear?\"",
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
        "try": "Think of a moment when you felt completely yourself. Remember where you were and how your body felt. Let that feeling fill you now.",
        "q": ["Where are you trying to fit in?", "What would you do differently if you stopped?"],
      },
      "14": {
        "intro": "This is Key 14, the Gift of Competence. When you work from love rather than pressure, effort turns into flow, and the results tend to take care of themselves.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 8, the Gift of Style, a reminder that how you do it is as much yours as what you do.",
        "try": "Think of something you love doing. Notice where in your body you feel the pleasure of it. Breathe into that spot and let it grow.",
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
        "try": "Take one slow, deliberate step, or simply press one foot into the floor, then the other. Feel how each one carries you forward.",
        "q": ["What small step could you take today?", "What's one step you've already taken that you haven't given yourself credit for?"],
      },
      "16": {
        "intro": "This is Key 16, the Gift of Versatility. You don't have to choose just one thing to be good at. Your many interests and talents are meant to be enjoyed.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 9, the Gift of Determination, which helps your gifts grow through gentle, steady practice.",
        "try": "Wiggle your fingers, roll your shoulders and let your face make a silly expression. Notice the lightness that comes with play.",
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
        "try": "Close your eyes and picture a dream you hold, in as much colour and detail as you can. Notice where in your body you feel it light up.",
        "q": ["Which dream came to mind first?", "Who would you need to say it to, and what would you say?"],
      },
      "12": {
        "intro": "This is Key 12, the Gift of Discrimination. Your words carry weight. Choosing them with care isn't holding back; it's letting what you say land where it's meant to.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 11, the Gift of Idealism. Courage needs something worth speaking for. Key 11 is the dream your words are here to serve.",
        "try": "Place your fingertips lightly on your throat and hum softly for a breath or two. Feel your voice. Then think of one true thing you'd like to say.",
        "q": ["What have you been holding back from saying?", "What dream sits underneath it?"],
      },
    },
  },
  {
    "a": "10", "b": "15",
    "aff": {"10": "I am at ease being myself.", "15": "Being myself is what draws life to me."},
    "lead": {
      "10": {
        "intro": "This is Key 10, the Gift of Naturalness. You don't have to work at being you. When you stop trying to be something else, a natural ease returns.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 15, the Gift of Magnetism: what that ease creates, people and opportunities that fit you, drawn in without effort.",
        "try": "Let your shoulders drop and your jaw soften. Breathe out slowly, a little longer than you breathe in. Notice what's left when you stop holding yourself up.",
        "q": ["Where do you feel most at ease?", "Who are you with, and what are you doing?"],
      },
      "15": {
        "intro": "This is Key 15, the Gift of Magnetism. You don't need to chase. When you're simply yourself, the right people and moments find their way to you.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 10, the Gift of Naturalness: the more comfortable you are in your own skin, the more life comes towards you.",
        "try": "Open your hands and rest them palms up. Take three easy breaths. Imagine, just for a moment, that what's meant for you is already on its way.",
        "q": ["What has come to you lately without you chasing it?", "Where could you stop chasing and let things come?"],
      },
    },
  },
  {
    "a": "17", "b": "18",
    "aff": {"17": "I see the bigger picture with my heart.", "18": "I grow with kindness towards myself."},
    "lead": {
      "17": {
        "intro": "This is Key 17, the Gift of Far-sightedness. The mind sees details, while the heart sees the whole story. Looking with your heart helps the small worries fall into place.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 18, the Gift of Integrity, which brings that same kindness to how you see yourself.",
        "try": "Bring a worry to mind. Now imagine looking back at it a year from now, from somewhere peaceful. Place a hand on your heart and take a slow breath. What feels different from there?",
        "q": ["What does your heart see that your mind was missing?"],
      },
      "18": {
        "intro": "This is Key 18, the Gift of Integrity. Wanting to improve is healthy. Criticising yourself along the way isn't needed. Growth flourishes in kindness.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 17, the Gift of Far-sightedness, a reminder that every stumble is part of a longer, kinder story.",
        "try": "Think of something you're being hard on yourself about. Now imagine a dear friend telling you the same thing about themselves. Notice how you'd speak to them, and say it quietly to yourself.",
        "q": ["How does it feel to be on your own side?"],
      },
    },
  },
  {
    "a": "19", "b": "33",
    "aff": {"19": "My sensitivity is a strength.", "33": "I see my patterns with gentle eyes."},
    "lead": {
      "19": {
        "intro": "This is Key 19, the Gift of Sensitivity. Feeling things deeply isn't a weakness. It's how you notice what others miss, and how you know what you need.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 33, the Gift of Mindfulness, which helps you understand your feelings without being swept away by them.",
        "try": "Close your eyes for a moment. Scan gently from head to toe and notice where you feel anything at all: warmth, tightness, tingling. Just notice, without changing it.",
        "q": ["What did your body tell you?", "What do you need right now?"],
      },
      "33": {
        "intro": "This is Key 33, the Gift of Mindfulness. We all repeat certain patterns. Seeing them clearly, and kindly, is the first step to choosing differently.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 19, the Gift of Sensitivity, which lets you notice those patterns in the first place.",
        "try": "Think of a pattern that keeps repeating. Imagine watching it like a scene in a film, from a comfortable seat. Breathe, and watch with curiosity rather than judgement.",
        "q": ["What might this pattern be trying to show you?"],
      },
    },
  },
  {
    "a": "20", "b": "34",
    "aff": {"20": "I am fully here, right now.", "34": "I have the strength my life asks of me."},
    "lead": {
      "20": {
        "intro": "This is Key 20, the Gift of Self-Assurance. Confidence lives in the present moment, not in planning or replaying. When you're fully here, you know what to do.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 34, the Gift of Strength: the energy that flows when you're present.",
        "try": "Feel your feet on the floor. Name three things you can see, two you can hear and one you can feel. Take a breath. You're here.",
        "q": ["What do you notice now that you've arrived in this moment?"],
      },
      "34": {
        "intro": "This is Key 34, the Gift of Strength. You have more in you than you think. Real strength isn't forcing. It's the natural power that rises when you're doing what's right for you.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 20, the Gift of Self-Assurance, a reminder that strength is easiest to find in the present.",
        "try": "Sit or stand tall, and press your feet firmly into the ground. Breathe low into your belly. Feel the steadiness that's already in you.",
        "q": ["What has your strength carried you through?", "Where does it feel easy, rather than forced?"],
      },
    },
  },
  {
    "a": "21",
    "b": "48",
    "aff": {
      "21": "I am the authority in my own life.",
      "48": "I have what I need to meet what comes."
    },
    "lead": {
      "21": {
        "intro": "This is Key 21, the Gift of Authority. You don't need anyone's permission to live your life your way. Real authority is quiet: it's simply taking charge of your own choices.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 48, the Gift of Resourcefulness: the inner wealth that backs up your choices.",
        "try": "Sit tall and rest your hands on your thighs. Say quietly, \"This is my life.\" Notice how your body responds: does it settle, or bristle?",
        "q": [
          "Where are you waiting for permission?",
          "What would you choose if it were entirely up to you?"
        ]
      },
      "48": {
        "intro": "This is Key 48, the Gift of Resourcefulness. When something new arrives, it's easy to feel you're not enough. But you have more inside you, more skills, wisdom and courage, than you realise.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 21, the Gift of Authority, which trusts you to use what you have.",
        "try": "Think of a challenge you've already come through. Remember one thing you did that helped. Breathe that memory into your chest and let it remind you.",
        "q": [
          "What's coming up that feels bigger than you?",
          "What have you already got that could help?"
        ]
      }
    }
  },
  {
    "a": "22",
    "b": "47",
    "aff": {
      "22": "I meet life with grace.",
      "47": "Every feeling I have becomes wisdom."
    },
    "lead": {
      "22": {
        "intro": "This is Key 22, the Gift of Graciousness. Grace isn't about being perfect. It's meeting whatever comes, the lovely and the difficult, with an open, gentle heart.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 47, the Gift of Transmutation: what grace makes possible, even hard feelings turning into understanding.",
        "try": "Let your face soften into the beginning of a smile. Breathe in, and as you breathe out, imagine you're saying \"yes\" to this moment, just as it is.",
        "q": [
          "What in your life could you meet more gently?"
        ]
      },
      "47": {
        "intro": "This is Key 47, the Gift of Transmutation. Difficult feelings aren't mistakes. Held kindly, they slowly change into something wiser, like compost becoming soil.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 22, the Gift of Graciousness: the gentle way to hold your feelings while they change.",
        "try": "Name a feeling you've had lately. Find where it lives in your body and rest a hand there. Breathe into it, without trying to fix it, and ask what it knows.",
        "q": [
          "What might this feeling be teaching you?"
        ]
      }
    }
  },
  {
    "a": "23",
    "b": "43",
    "aff": {
      "23": "I keep it simple.",
      "43": "My inner voice knows."
    },
    "lead": {
      "23": {
        "intro": "This is Key 23, the Gift of Simplicity. When life feels complicated, the answer is often simpler than we think. Clarity comes from stripping things back to what's true.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 43, the Gift of Insight: the clear inner knowing that simplicity makes room for.",
        "try": "Take one deep breath and let it all go with a sigh. Ask yourself, \"What's the simplest thing that's true right now?\" Wait for the first answer.",
        "q": [
          "What are you overcomplicating?",
          "What would the simple version look like?"
        ]
      },
      "43": {
        "intro": "This is Key 43, the Gift of Insight. Answers often arrive suddenly, in the shower, on a walk or half asleep. That quiet inner voice knows more than the busy mind.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 23, the Gift of Simplicity, which helps you share your insight in a way others can hear.",
        "try": "Close your eyes and place a hand over your ear, as if listening inwards. Ask a question you've been wondering about. Notice the very first word or image that comes.",
        "q": [
          "When has your inner voice been right before?",
          "What is it saying now?"
        ]
      }
    }
  },
  {
    "a": "24",
    "b": "44",
    "aff": {
      "24": "I welcome the quiet space where new ideas arrive.",
      "44": "I recognise my true allies."
    },
    "lead": {
      "24": {
        "intro": "This is Key 24, the Gift of Invention. New ideas rarely come when we're straining for them. They arrive in the pauses, when the mind finally rests.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 44, the Gift of Teamwork, which brings your ideas to life with the right people beside you.",
        "try": "Let your eyes go soft and unfocused, as if gazing at a far horizon. Breathe slowly. For a few breaths, don't think about anything. Just leave space.",
        "q": [
          "Where can you make more quiet space in your day?"
        ]
      },
      "44": {
        "intro": "This is Key 44, the Gift of Teamwork. Some people simply fit. Your instincts can recognise who's truly on your side, and who brings out your best.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 24, the Gift of Invention, which gives your partnerships fresh ideas to grow from.",
        "try": "Bring to mind three people in your life, one at a time. Notice how your body responds to each: lighter, heavier, warmer, tighter. Trust what you feel.",
        "q": [
          "Who leaves you feeling more like yourself?",
          "How could you spend more time with them?"
        ]
      }
    }
  },
  {
    "a": "25",
    "b": "46",
    "aff": {
      "25": "I have the courage to feel what I feel.",
      "46": "I delight in being alive in my body."
    },
    "lead": {
      "25": {
        "intro": "This is Key 25, the Gift of Acceptance. Feelings aren't right or wrong. Letting yourself feel them, fully and kindly, takes courage, and it's how they move through.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 46, the Gift of Delight: what opens up when you stop pushing feelings away, the simple pleasure of being alive.",
        "try": "Place one hand on your chest and one on your belly. Breathe slowly and say silently, \"Whatever I'm feeling is welcome.\" Let it be there, just as it is.",
        "q": [
          "What feeling have you been holding at arm's length?",
          "What happens when you let it in?"
        ]
      },
      "46": {
        "intro": "This is Key 46, the Gift of Delight. Your body isn't just something that carries you around. It's how you taste, touch, move and feel the joy of being here.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 25, the Gift of Acceptance, which lets every part of you be welcome, so delight can flow freely.",
        "try": "Stretch slowly in whatever way your body wants to. Notice one sensation that feels good: warmth, softness, a loosening. Linger there for a breath or two.",
        "q": [
          "What does your body love?",
          "When did you last give it that?"
        ]
      }
    }
  },
  {
    "a": "26",
    "b": "45",
    "aff": {
      "26": "I speak from my heart's true intention.",
      "45": "Together, we are more."
    },
    "lead": {
      "26": {
        "intro": "This is Key 26, the Gift of Artfulness. When your words come from your heart, people feel it. You don't need to persuade or impress, only to mean what you say.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 45, the Gift of Synergy: what heartfelt words create, real connection and shared purpose.",
        "try": "Place a hand on your heart. Think of something you want to say to someone. Before you speak, ask your heart, \"What do I really mean?\" Notice the answer.",
        "q": [
          "What would you say if you were speaking purely from your heart?"
        ]
      },
      "45": {
        "intro": "This is Key 45, the Gift of Synergy. Some things can't be done alone, and don't need to be. When people bring their gifts together, something greater becomes possible.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 26, the Gift of Artfulness: how you invite others in honestly.",
        "try": "Think of someone you'd love to create something with. Picture the two of you side by side. Breathe, and notice how it feels not to have to do it all yourself.",
        "q": [
          "Who could you share the load with?",
          "What might you create together?"
        ]
      }
    }
  },
  {
    "a": "27",
    "b": "28",
    "aff": {
      "27": "I give freely and with joy.",
      "28": "I embrace all of who I am, light and shadow."
    },
    "lead": {
      "27": {
        "intro": "This is Key 27, the Gift of Altruism. Real giving comes from fullness, not obligation. When you give because you want to, it nourishes you as much as the person receiving.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 28, the Gift of Totality, a reminder to include yourself in your care.",
        "try": "Cup your hands together in front of you, as if holding something precious. Imagine filling them first for yourself, then offering what overflows to someone you love.",
        "q": [
          "Are you giving from fullness or from emptiness right now?",
          "How could you receive a little more?"
        ]
      },
      "28": {
        "intro": "This is Key 28, the Gift of Totality. You don't have to hide the messy, difficult parts of yourself. Every part has a story, and every part belongs.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 27, the Gift of Altruism, which flows more freely when you're no longer spending energy hiding.",
        "try": "Wrap your arms around yourself in a gentle hug. Breathe in, and as you breathe out, say silently, \"All of me is welcome here.\"",
        "q": [
          "Which part of you have you been keeping in the dark?",
          "What might it need from you?"
        ]
      }
    }
  },
  {
    "a": "29",
    "b": "30",
    "aff": {
      "29": "I commit to myself, again and again.",
      "30": "I hold my desires lightly."
    },
    "lead": {
      "29": {
        "intro": "This is Key 29, the Gift of Commitment. Commitment isn't a single promise. It's saying yes to yourself again each day, especially on the days it's hard.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 30, the Gift of Lightness, which keeps your commitment joyful rather than heavy.",
        "try": "Place both hands on your belly and feel it rise and fall. With each breath out, say silently, \"Yes.\" Let each yes be to you.",
        "q": [
          "What would it mean to choose yourself today?",
          "What are you ready to recommit to?"
        ]
      },
      "30": {
        "intro": "This is Key 30, the Gift of Lightness. Wanting things is natural. Holding them lightly means enjoying the longing without needing everything to happen right now.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 29, the Gift of Commitment, which keeps you steady while your desires unfold.",
        "try": "Hold out an open palm and imagine a feather resting on it. Feel how lightly you'd hold it so it doesn't blow away or get crushed. Hold your wishes like that.",
        "q": [
          "What are you longing for?",
          "How would it feel to hold that longing more lightly?"
        ]
      }
    }
  },
  {
    "a": "31",
    "b": "41",
    "aff": {
      "31": "My voice helps others rise.",
      "41": "I feel a new beginning stirring in me."
    },
    "lead": {
      "31": {
        "intro": "This is Key 31, the Gift of Leadership. True leaders don't push from the front. They speak up for what matters, and others feel stronger for hearing it.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 41, the Gift of Anticipation: the fresh vision that gives your voice something worth saying.",
        "try": "Sit tall, breathe into your chest and let your voice out on a gentle \"ahh\". Feel it resonate. Notice that your voice has its own natural strength.",
        "q": [
          "Who could your words encourage today?",
          "What do you want to speak up for?"
        ]
      },
      "41": {
        "intro": "This is Key 41, the Gift of Anticipation. Before anything new arrives, there's a feeling, a flutter of possibility. Trust it, even before you know what it is.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 31, the Gift of Leadership, which will one day give your new beginning a voice.",
        "try": "Close your eyes and imagine a seed under the soil, just starting to stir. Place a hand low on your belly and breathe into it. Notice any flicker of excitement or possibility.",
        "q": [
          "What new beginning can you sense?",
          "What would help it grow?"
        ]
      }
    }
  },
  {
    "a": "32",
    "b": "42",
    "aff": {
      "32": "I build what truly lasts.",
      "42": "I let life unfold in its own way."
    },
    "lead": {
      "32": {
        "intro": "This is Key 32, the Gift of Preservation. Some things are worth tending slowly: relationships, skills, homes, dreams. What you nurture with care tends to endure.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 42, the Gift of Detachment, which lets you build without gripping too tightly.",
        "try": "Rest both hands on a solid surface, a table or your knees. Feel its steadiness. Breathe, and think of one thing in your life you'd like to last.",
        "q": [
          "What deserves more of your patient care?",
          "What could you tend a little today?"
        ]
      },
      "42": {
        "intro": "This is Key 42, the Gift of Detachment. Not everything needs managing. Some things simply need time and trust, and the freedom to finish in their own way.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 32, the Gift of Preservation, a reminder that letting go and taking care go hand in hand.",
        "try": "Take a full breath in. As you breathe out, let your hands fall open in your lap. Imagine putting something down that you don't need to carry right now.",
        "q": [
          "What are you trying to control?",
          "What might happen if you let it unfold?"
        ]
      }
    }
  },
  {
    "a": "37",
    "b": "40",
    "aff": {
      "37": "I give from a full cup.",
      "40": "My no is as worthy of respect as my yes."
    },
    "lead": {
      "40": {
        "intro": "This is Key 40, the Gift of Resolve. Saying no isn't selfish. It's how you protect your energy, so that your yes can be wholehearted.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 37, the Gift of Equality: what your no makes possible, giving that doesn't drain you.",
        "try": "Sit tall and say a quiet, clear \"no\" out loud. Notice how it feels in your body. Then say \"yes\", and notice the difference. Both belong to you.",
        "q": [
          "What do you need to say no to?",
          "What would that make space for?"
        ]
      },
      "37": {
        "intro": "This is Key 37, the Gift of Equality. Caring for others works best when you're cared for too. Relationships thrive when giving and receiving flow both ways.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 40, the Gift of Resolve, which keeps your cup full by honouring your limits.",
        "try": "Imagine a cup inside your chest. Breathe in and picture it filling with warmth. Keep breathing until it feels full, then notice how it feels to have something to share.",
        "q": [
          "How full is your cup right now?",
          "What would fill it?"
        ]
      }
    }
  },
  {
    "a": "38",
    "b": "39",
    "aff": {
      "38": "I meet my challenges with heart.",
      "39": "My energy is alive and creative."
    },
    "lead": {
      "38": {
        "intro": "This is Key 38, the Gift of Perseverance. Some challenges ask us to keep going. When you fight for what you love rather than against what you fear, the struggle gains meaning.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 39, the Gift of Dynamism: the spark that keeps you going.",
        "try": "Think of a challenge you're facing. Place a hand on your heart and ask, \"What do I love that this is for?\" Breathe that love into your chest.",
        "q": [
          "What makes this challenge worth meeting?"
        ]
      },
      "39": {
        "intro": "This is Key 39, the Gift of Dynamism. Restlessness and frustration are often creative energy looking for somewhere to go. Give it an outlet, and it comes alive.",
        "partner": "Every Gene Key has a partner, its other half. Yours is Key 38, the Gift of Perseverance, which gives that energy a purpose worth pursuing.",
        "try": "Shake out your hands, then your arms and shoulders, for ten seconds. Stop, stand still and feel the buzz of energy in your body.",
        "q": [
          "Where is your energy wanting to go?",
          "What would you love to put it into?"
        ]
      }
    }
  },
]

e = html.escape

def journey(card, lead, other):
    L = card["lead"][lead]
    q = "<br>".join(e(x) for x in L["q"])
    practice = ""
    if L.get("try"):
        practice = f'''    <div class="step">
      <p class="label">Try this</p>
      <p class="practice">{e(L["try"])}</p>
    </div>
'''
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
{practice}    <div class="step">
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
    <h2>If this was hard to reach</h2>
    <p>Some shifts come more easily with someone beside you. I'm Phoebe, of Radiant Oracle: a PSYCH-K® coach, Human Design and Gene Keys coach, astrologer and tarot coach. I work one to one and in groups, helping you change the beliefs that hold you back and read your own life more clearly.</p>
    <p>Follow along on Instagram for more practices, or message me there to see how I can help.</p>
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
