import html, os, sys

ROOT = sys.argv[1]

CARDS = [
  {
    "a": "1",
    "b": "2",
    "aff": {
      "1": "I let my creative fire burn bright.",
      "2": "Life knows the way, and so do I."
    },
    "lead": {
      "1": {
        "intro": "This is Key 1, Creative Spark. There's a spark in you that's entirely your own, not borrowed or copied. It doesn't need permission to shine.",
        "partner": "Every key has a partner, its other half. Yours is Key 2, Inner Compass: the quiet inner compass that lets your fire move in the right direction without forcing it.",
        "try": "Place a hand just below your ribs and breathe into it. Imagine a small warm flame there, growing a little brighter with each breath in. Notice what it wants to light up.",
        "q": [
          "What lights me up lately?",
          "Where does it seem to want to go?"
        ]
      },
      "2": {
        "intro": "This is Key 2, Inner Compass. You don't have to map every step. Something in you already knows the direction, even when the path isn't visible yet.",
        "partner": "Every key has a partner, its other half. Yours is Key 1, Creative Spark: the spark that makes the journey worth taking.",
        "try": "Close your eyes and let your body sway very slightly, side to side, until it finds its own still centre. Rest there. Notice the quiet sense of which way feels right.",
        "q": [
          "Where have I lost my way?",
          "What would trusting the direction feel like?"
        ]
      }
    }
  },
  {
    "a": "3",
    "b": "50",
    "aff": {
      "3": "I meet change with curiosity.",
      "50": "I stay steady at my centre."
    },
    "lead": {
      "3": {
        "intro": "This is Key 3, Curious Change. Change can feel like chaos, but it's often something new trying to be born. Curiosity turns it from a threat into a doorway.",
        "partner": "Every key has a partner, its other half. Yours is Key 50, Steady Centre: the still point that lets you meet change without losing yourself.",
        "try": "Think of something that's changing. Instead of tensing, raise your eyebrows slightly, as if you're curious, and breathe out. Ask yourself, \"I wonder what this could become?\"",
        "q": [
          "What's changing?",
          "What might it be making room for?"
        ]
      },
      "50": {
        "intro": "This is Key 50, Steady Centre. Whatever is moving around you, there's a place inside that stays calm and fair. Coming back to it is always possible.",
        "partner": "Every key has a partner, its other half. Yours is Key 3, Curious Change, a reminder that steadiness isn't standing still. It's what lets you welcome the new.",
        "try": "Sit tall and place both hands on your lower belly. Breathe slowly in for four, out for six, three times. Feel the steady place that stays calm underneath everything.",
        "q": [
          "Where is my centre right now?",
          "What helps me find my way back to it?"
        ]
      }
    }
  },
  {
    "a": "4",
    "b": "49",
    "aff": {
      "4": "I seek to understand before I answer.",
      "49": "I am free to let old patterns go."
    },
    "lead": {
      "4": {
        "intro": "This is Key 4, Listening Mind. The mind loves quick answers, but real understanding takes a breath first. It listens for the whole picture.",
        "partner": "Every key has a partner, its other half. Yours is Key 49, Letting Go: what understanding makes possible, the freedom to change what no longer serves you.",
        "try": "Before answering anything today, try one slow breath first. Practise now: think of a question on your mind, breathe in and out slowly, and notice what arrives in the pause.",
        "q": [
          "What question am I rushing to answer?",
          "What might I see if I waited a little longer?"
        ]
      },
      "49": {
        "intro": "This is Key 49, Letting Go. Some habits, roles and relationships belonged to an earlier version of you. Letting them go isn't rejection. It's growth.",
        "partner": "Every key has a partner, its other half. Yours is Key 4, Listening Mind, which lets you release things with clarity rather than in a rush.",
        "try": "Make a loose fist, as if you're holding on to an old habit. Breathe in. As you breathe out, slowly open your hand. Notice how it feels to let go.",
        "q": [
          "Which old pattern is ready to go?",
          "What do I understand now that I didn't before?"
        ]
      }
    }
  },
  {
    "a": "5",
    "b": "35",
    "aff": {
      "5": "I trust the rhythm of my life.",
      "35": "My life is an adventure, just as it is."
    },
    "lead": {
      "5": {
        "intro": "This is Key 5, Natural Rhythm. Life moves in seasons, not straight lines. What feels like waiting is often things quietly ripening.",
        "partner": "Every key has a partner, its other half. Yours is Key 35, Everyday Wonder, which finds the richness in each moment along the way.",
        "try": "Place a hand on your chest and feel your heartbeat or breath for a few moments. Let it set the pace. There's nowhere to rush to right now.",
        "q": [
          "Where am I pushing, instead of pausing to see what comes to me?",
          "What might show up if I waited a moment before acting?"
        ]
      },
      "35": {
        "intro": "This is Key 35, Everyday Wonder. Adventure isn't always somewhere new. It's meeting your own life with fresh eyes and noticing what's already here.",
        "partner": "Every key has a partner, its other half. Yours is Key 5, Natural Rhythm, which lets the adventure unfold in its own time.",
        "try": "Look around you as if you've just arrived somewhere new for the very first time. Find one thing you've never really noticed before.",
        "q": [
          "What in my life right now is quietly remarkable?",
          "What would change if I saw it that way?"
        ]
      }
    }
  },
  {
    "a": "6",
    "b": "36",
    "aff": {
      "6": "I soften and stay true to myself.",
      "36": "My heart stays open, whatever life brings."
    },
    "lead": {
      "6": {
        "intro": "This is Key 6, Soft Strength. Softening isn't giving in. It's choosing warmth over winning, while still knowing where you stand.",
        "partner": "Every key has a partner, its other half. Yours is Key 36, Open Heart: the open heart that makes softening possible.",
        "try": "Notice where you're holding tension: jaw, shoulders, hands. Breathe into that place and let it soften by just ten percent. Notice that you're still you.",
        "q": [
          "Where am I bracing for a fight?",
          "What might happen if I softened, just a little?"
        ]
      },
      "36": {
        "intro": "This is Key 36, Open Heart. Hard times can make us close up to protect ourselves. Staying open is a quiet kind of courage, and it lets life keep reaching you.",
        "partner": "Every key has a partner, its other half. Yours is Key 6, Soft Strength, which shows you can stay open and still hold your ground.",
        "try": "Place a hand on your heart and breathe gently into it. Imagine it softening and widening a little with each breath, like a door easing open.",
        "q": [
          "What has made me want to close up lately?",
          "What would help my heart feel safe enough to stay open?"
        ]
      }
    }
  },
  {
    "a": "7",
    "b": "13",
    "aff": {
      "7": "I lead simply by being myself.",
      "13": "I listen deeply, to others and to me."
    },
    "lead": {
      "7": {
        "intro": "This is Key 7, Quiet Leadership. You don't need a title to lead. When you live true to yourself, others quietly find their way by your example.",
        "partner": "Every key has a partner, its other half. Yours is Key 13, Deep Listening: the listening that makes your guidance wise.",
        "try": "Stand or sit tall, chin level, shoulders relaxed. Take a breath and feel what it's like to simply take up your own space.",
        "q": [
          "Who might be watching how I live?",
          "What am I showing them without saying a word?"
        ]
      },
      "13": {
        "intro": "This is Key 13, Deep Listening. Real listening means hearing what's said and what's underneath it, including your own inner voice.",
        "partner": "Every key has a partner, its other half. Yours is Key 7, Quiet Leadership: what deep listening grows into, knowing which way to go.",
        "try": "Close your eyes and listen to the furthest sound you can hear, then the nearest, then the sound of your own breath. Ask yourself quietly, \"What do I need to hear?\"",
        "q": [
          "Who in my life needs to be truly heard?",
          "What has my own inner voice been trying to tell me?"
        ]
      }
    }
  },
  {
    "a": "8",
    "b": "14",
    "aff": {
      "8": "I dare to be unmistakably me.",
      "14": "I do what I love, and I do it well."
    },
    "lead": {
      "8": {
        "intro": "This is Key 8, True Colours. There's no one else quite like you, and the world doesn't need a copy of anyone. Being yourself is your greatest contribution.",
        "partner": "Every key has a partner, its other half. Yours is Key 14, Joyful Work: what happens when you put your true self into your work.",
        "try": "Think of a moment when you felt completely yourself. Remember where you were and how your body felt. Let that feeling fill you now.",
        "q": [
          "Where am I trying to fit in?",
          "What would I do differently if I stopped?"
        ]
      },
      "14": {
        "intro": "This is Key 14, Joyful Work. When you work from love rather than pressure, effort turns into flow, and the results tend to take care of themselves.",
        "partner": "Every key has a partner, its other half. Yours is Key 8, True Colours, a reminder that how you do it is as much yours as what you do.",
        "try": "Think of something you love doing. Notice where in your body you feel the pleasure of it. Breathe into that spot and let it grow.",
        "q": [
          "What do I do that makes time disappear?",
          "How could I make a little more room for it?"
        ]
      }
    }
  },
  {
    "a": "9",
    "b": "16",
    "aff": {
      "9": "Every small step I take matters.",
      "16": "I am free to play with all my gifts."
    },
    "lead": {
      "9": {
        "intro": "This is Key 9, Small Steps. Big changes are built from small, steady steps. Each one counts, even when you can't see the difference yet.",
        "partner": "Every key has a partner, its other half. Yours is Key 16, Playful Gifts, which brings lightness and enjoyment to the steps along the way.",
        "try": "Take one slow, deliberate step, or simply press one foot into the floor, then the other. Feel how each one carries you forward.",
        "q": [
          "What small step could I take today?",
          "What's one step I've already taken that I haven't given myself credit for?"
        ]
      },
      "16": {
        "intro": "This is Key 16, Playful Gifts. You don't have to choose just one thing to be good at. Your many interests and talents are meant to be enjoyed.",
        "partner": "Every key has a partner, its other half. Yours is Key 9, Small Steps, which helps your gifts grow through gentle, steady practice.",
        "try": "Wiggle your fingers, roll your shoulders and let your face make a silly expression. Notice the lightness that comes with play.",
        "q": [
          "What do I love doing that I've set aside?",
          "What would it feel like to play with it again?"
        ]
      }
    }
  },
  {
    "a": "10",
    "b": "15",
    "aff": {
      "10": "I am at ease being myself.",
      "15": "Being myself is what draws life to me."
    },
    "lead": {
      "10": {
        "intro": "This is Key 10, Easy Being. You don't have to work at being you. When you stop trying to be something else, a natural ease returns.",
        "partner": "Every key has a partner, its other half. Yours is Key 15, Gentle Pull: what that ease creates, people and opportunities that fit you, drawn in without effort.",
        "try": "Let your shoulders drop and your jaw soften. Breathe out slowly, a little longer than you breathe in. Notice what's left when you stop holding yourself up.",
        "q": [
          "Where do I feel most at ease?",
          "Who am I with, and what am I doing?"
        ]
      },
      "15": {
        "intro": "This is Key 15, Gentle Pull. You don't need to chase. When you're simply yourself, the right people and moments find their way to you.",
        "partner": "Every key has a partner, its other half. Yours is Key 10, Easy Being: the more comfortable you are in your own skin, the more life comes towards you.",
        "try": "Open your hands and rest them palms up. Take three easy breaths. Imagine, just for a moment, that what's meant for you is already on its way.",
        "q": [
          "What has come to me lately without me chasing it?",
          "Where could I stop chasing and let things come?"
        ]
      }
    }
  },
  {
    "a": "11",
    "b": "12",
    "aff": {
      "11": "I honour the dreams that light me up.",
      "12": "I choose my words with care and courage."
    },
    "lead": {
      "11": {
        "intro": "This is Key 11, Guiding Dreams. Somewhere in you is a picture of how life could be. It isn't a fantasy to grow out of. It's a light to steer by.",
        "partner": "Every key has a partner, its other half. Yours is Key 12, Brave Words. A dream stays a dream until it's spoken. Key 12 is the voice that gives your vision shape: what to say, when, and to whom.",
        "try": "Close your eyes and picture a dream you hold, in as much colour and detail as you can. Notice where in your body you feel it light up.",
        "q": [
          "Which dream came to mind first?",
          "What's one small step towards it? And when I'm ready, who could I share it with?"
        ]
      },
      "12": {
        "intro": "This is Key 12, Brave Words. Your words carry weight. Choosing them with care isn't holding back; it's letting what you say land where it's meant to.",
        "partner": "Every key has a partner, its other half. Yours is Key 11, Guiding Dreams. Courage needs something worth speaking for. Key 11 is the dream your words are here to serve.",
        "try": "Place your fingertips lightly on your throat and hum softly for a breath or two. Feel your voice. Then think of one true thing you'd like to say.",
        "q": [
          "What have I been holding back from saying?",
          "What truth sits underneath it?"
        ]
      }
    }
  },
  {
    "a": "17",
    "b": "18",
    "aff": {
      "17": "I see the bigger picture with my heart.",
      "18": "I grow with kindness towards myself."
    },
    "lead": {
      "17": {
        "intro": "This is Key 17, Heart's View. The mind sees details, while the heart sees the whole story. Looking with your heart helps the small worries fall into place.",
        "partner": "Every key has a partner, its other half. Yours is Key 18, Kind Growth, which brings that same kindness to how you see yourself.",
        "try": "Bring a worry to mind. Now imagine looking back at it a year from now, from somewhere peaceful. Place a hand on your heart and take a slow breath. What feels different from there?",
        "q": [
          "From that peaceful place, what can I see in my heart that matters most?"
        ]
      },
      "18": {
        "intro": "This is Key 18, Kind Growth. Wanting to improve is healthy. Criticising yourself along the way isn't needed. Growth flourishes in kindness.",
        "partner": "Every key has a partner, its other half. Yours is Key 17, Heart's View, a reminder that every stumble is part of a longer, kinder story.",
        "try": "Think of something you're being hard on yourself about. Now imagine a dear friend telling you the same thing about themselves. Notice how you'd speak to them, and say it quietly to yourself.",
        "q": [
          "What changes when I speak to myself the way I'd speak to a friend?"
        ]
      }
    }
  },
  {
    "a": "19",
    "b": "33",
    "aff": {
      "19": "My sensitivity is a strength.",
      "33": "I see my patterns with gentle eyes."
    },
    "lead": {
      "19": {
        "intro": "This is Key 19, Tender Strength. Feeling things deeply isn't a weakness. It's how you notice what others miss, and how you know what you need.",
        "partner": "Every key has a partner, its other half. Yours is Key 33, Gentle Seeing, which helps you understand your feelings without being swept away by them.",
        "try": "Close your eyes for a moment. Scan gently from head to toe and notice where you feel anything at all: warmth, tightness, tingling. Just notice, without changing it.",
        "q": [
          "What did my body tell me?",
          "What do I need right now?"
        ]
      },
      "33": {
        "intro": "This is Key 33, Gentle Seeing. We all repeat certain patterns. Seeing them clearly, and kindly, is the first step to choosing differently.",
        "partner": "Every key has a partner, its other half. Yours is Key 19, Tender Strength, which lets you notice those patterns in the first place.",
        "try": "Think of a pattern that keeps repeating. Imagine watching it like a scene in a film, from a comfortable seat. Breathe, and watch with curiosity rather than judgement.",
        "q": [
          "What might this pattern be trying to show me?"
        ]
      }
    }
  },
  {
    "a": "20",
    "b": "34",
    "aff": {
      "20": "I am fully here, right now.",
      "34": "I have the strength my life asks of me."
    },
    "lead": {
      "20": {
        "intro": "This is Key 20, Here and Now. Confidence lives in the present moment, not in planning or replaying. When you're fully here, you know what to do.",
        "partner": "Every key has a partner, its other half. Yours is Key 34, Natural Power: the energy that flows when you're present.",
        "try": "Feel your feet on the floor. Name three things you can see, two you can hear and one you can feel. Take a breath. You're here.",
        "q": [
          "What do I notice now that I've arrived in this moment?"
        ]
      },
      "34": {
        "intro": "This is Key 34, Natural Power. You have more in you than you think. Real strength isn't forcing. It's the natural power that rises when you're doing what's right for you.",
        "partner": "Every key has a partner, its other half. Yours is Key 20, Here and Now, a reminder that strength is easiest to find in the present.",
        "try": "Sit or stand tall, and press your feet firmly into the ground. Breathe low into your belly. Feel the steadiness that's already in you.",
        "q": [
          "What has my strength carried me through?",
          "Where does it feel easy, rather than forced?"
        ]
      }
    }
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
        "intro": "This is Key 21, Owning My Life. You don't need anyone's permission to live your life your way. Real authority is quiet: it's simply taking charge of your own choices.",
        "partner": "Every key has a partner, its other half. Yours is Key 48, Inner Wealth: the inner wealth that backs up your choices.",
        "try": "Sit tall and rest your hands on your thighs. Say quietly, \"This is my life.\" Notice how your body responds: does it settle, or bristle?",
        "q": [
          "Where am I waiting for permission?",
          "What would I choose if it were entirely up to me?"
        ]
      },
      "48": {
        "intro": "This is Key 48, Inner Wealth. When something new arrives, it's easy to feel you're not enough. But you have more inside you, more skills, wisdom and courage, than you realise.",
        "partner": "Every key has a partner, its other half. Yours is Key 21, Owning My Life, which trusts you to use what you have.",
        "try": "Think of a challenge you've already come through. Remember one thing you did that helped. Breathe that memory into your chest and let it remind you.",
        "q": [
          "What's coming up that feels bigger than me?",
          "What do I already have, within me or around me, that could help?"
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
        "intro": "This is Key 22, Gentle Grace. Grace isn't about being perfect. It's meeting whatever comes, the lovely and the difficult, with an open, gentle heart.",
        "partner": "Every key has a partner, its other half. Yours is Key 47, Feeling into Wisdom: what grace makes possible, even hard feelings turning into understanding.",
        "try": "Let your face soften into the beginning of a smile. Breathe in, and as you breathe out, imagine you're saying \"yes\" to this moment, just as it is.",
        "q": [
          "What in my life could I meet more gently?"
        ]
      },
      "47": {
        "intro": "This is Key 47, Feeling into Wisdom. Difficult feelings aren't mistakes. Held kindly, they slowly change into something wiser, like compost becoming soil.",
        "partner": "Every key has a partner, its other half. Yours is Key 22, Gentle Grace: the gentle way to hold your feelings while they change.",
        "try": "Name a feeling you've had lately. Find where it lives in your body and rest a hand there. Breathe into it, without trying to fix it, and ask what it knows.",
        "q": [
          "What might this feeling be teaching me?"
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
        "intro": "This is Key 23, Simple Truth. When life feels complicated, the answer is often simpler than we think. Clarity comes from stripping things back to what's true.",
        "partner": "Every key has a partner, its other half. Yours is Key 43, Inner Voice: the clear inner knowing that simplicity makes room for.",
        "try": "Take one deep breath and let it all go with a sigh. Ask yourself, \"What's the simplest thing that's true right now?\" Wait for the first answer.",
        "q": [
          "What am I overcomplicating?",
          "What would the simple version look like?"
        ]
      },
      "43": {
        "intro": "This is Key 43, Inner Voice. Answers often arrive suddenly, in the shower, on a walk or half asleep. That quiet inner voice knows more than the busy mind.",
        "partner": "Every key has a partner, its other half. Yours is Key 23, Simple Truth, which helps you share your insight in a way others can hear.",
        "try": "Close your eyes and place a hand over your ear, as if listening inwards. Ask a question you've been wondering about. Notice the very first word or image that comes.",
        "q": [
          "When has my inner voice been right before?",
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
        "intro": "This is Key 24, Quiet Space. New ideas rarely come when we're straining for them. They arrive in the pauses, when the mind finally rests.",
        "partner": "Every key has a partner, its other half. Yours is Key 44, True Allies, which brings your ideas to life with the right people beside you.",
        "try": "Let your eyes go soft and unfocused, as if gazing at a far horizon. Breathe slowly. For a few breaths, don't think about anything. Just leave space.",
        "q": [
          "Where can I make more quiet space in my day?"
        ]
      },
      "44": {
        "intro": "This is Key 44, True Allies. Some people simply fit. Your instincts can recognise who's truly on your side, and who brings out your best.",
        "partner": "Every key has a partner, its other half. Yours is Key 24, Quiet Space, which gives your partnerships fresh ideas to grow from.",
        "try": "Bring to mind three people in your life, one at a time. Notice how your body responds to each: lighter, heavier, warmer, tighter. Trust what you feel.",
        "q": [
          "Who leaves me feeling more like myself?",
          "How could I spend more time with them?"
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
        "intro": "This is Key 25, Brave Feeling. Feelings aren't right or wrong. Letting yourself feel them, fully and kindly, takes courage, and it's how they move through.",
        "partner": "Every key has a partner, its other half. Yours is Key 46, Body Joy: what opens up when you stop pushing feelings away, the simple pleasure of being alive.",
        "try": "Place one hand on your chest and one on your belly. Breathe slowly and say silently, \"Whatever I'm feeling is welcome.\" Let it be there, just as it is.",
        "q": [
          "What feeling have I been holding at arm's length?",
          "What happens when I let it in?"
        ]
      },
      "46": {
        "intro": "This is Key 46, Body Joy. Your body isn't just something that carries you around. It's how you taste, touch, move and feel the joy of being here.",
        "partner": "Every key has a partner, its other half. Yours is Key 25, Brave Feeling, which lets every part of you be welcome, so delight can flow freely.",
        "try": "Stretch slowly in whatever way your body wants to. Notice one sensation that feels good: warmth, softness, a loosening. Linger there for a breath or two.",
        "q": [
          "What does my body love?",
          "When did I last give it that?"
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
        "intro": "This is Key 26, Heartfelt Words. When your words come from your heart, people feel it. You don't need to persuade or impress, only to mean what you say.",
        "partner": "Every key has a partner, its other half. Yours is Key 45, Shared Purpose: what heartfelt words create, real connection and shared purpose.",
        "try": "Place a hand on your heart. Think of something you want to say to someone. Before you speak, ask your heart, \"What do I really mean?\" Notice the answer.",
        "q": [
          "What would I say if I were speaking purely from my heart?"
        ]
      },
      "45": {
        "intro": "This is Key 45, Shared Purpose. Some things can't be done alone, and don't need to be. When people bring their gifts together, something greater becomes possible.",
        "partner": "Every key has a partner, its other half. Yours is Key 26, Heartfelt Words: how you invite others in honestly.",
        "try": "Think of someone you'd love to create something with. Picture the two of you side by side. Breathe, and notice how it feels not to have to do it all yourself.",
        "q": [
          "Who could I share the load with?",
          "What might we create together?"
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
        "intro": "This is Key 27, Overflowing Care. Real giving comes from fullness, not obligation. When you give because you want to, it nourishes you as much as the person receiving.",
        "partner": "Every key has a partner, its other half. Yours is Key 28, Whole Self, a reminder to include yourself in your care.",
        "try": "Cup your hands together in front of you, as if holding something precious. Imagine filling them first for yourself, then offering what overflows to someone you love.",
        "q": [
          "Am I giving from fullness or from emptiness right now?",
          "How could I receive a little more?"
        ]
      },
      "28": {
        "intro": "This is Key 28, Whole Self. You don't have to hide the messy, difficult parts of yourself. Every part has a story, and every part belongs.",
        "partner": "Every key has a partner, its other half. Yours is Key 27, Overflowing Care, which flows more freely when you're no longer spending energy hiding.",
        "try": "Wrap your arms around yourself in a gentle hug. Breathe in, and as you breathe out, say silently, \"All of me is welcome here.\"",
        "q": [
          "Which part of me have I been keeping in the dark?",
          "What might it need from me?"
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
        "intro": "This is Key 29, Daily Yes. Commitment isn't a single promise. It's saying yes to yourself again each day, especially on the days it's hard.",
        "partner": "Every key has a partner, its other half. Yours is Key 30, Light Longing, which keeps your commitment joyful rather than heavy.",
        "try": "Place both hands on your belly and feel it rise and fall. With each breath out, say silently, \"Yes.\" Let each yes be to you.",
        "q": [
          "What would it mean to choose myself today?",
          "What am I ready to recommit to?"
        ]
      },
      "30": {
        "intro": "This is Key 30, Light Longing. Wanting things is natural. Holding them lightly means enjoying the longing without needing everything to happen right now.",
        "partner": "Every key has a partner, its other half. Yours is Key 29, Daily Yes, which keeps you steady while your desires unfold.",
        "try": "Hold out an open palm and imagine a feather resting on it. Feel how lightly you'd hold it so it doesn't blow away or get crushed. Hold your wishes like that.",
        "q": [
          "What am I longing for?",
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
        "intro": "This is Key 31, Uplifting Voice. True leaders don't push from the front. They speak up for what matters, and others feel stronger for hearing it.",
        "partner": "Every key has a partner, its other half. Yours is Key 41, New Beginnings: the fresh vision that gives your voice something worth saying.",
        "try": "Sit tall, breathe into your chest and let your voice out on a gentle \"ahh\". Feel it resonate. Notice that your voice has its own natural strength.",
        "q": [
          "Who could my words encourage today?",
          "What do I want to speak up for?"
        ]
      },
      "41": {
        "intro": "This is Key 41, New Beginnings. Before anything new arrives, there's a feeling, a flutter of possibility. Trust it, even before you know what it is.",
        "partner": "Every key has a partner, its other half. Yours is Key 31, Uplifting Voice, which will one day give your new beginning a voice.",
        "try": "Close your eyes and imagine a seed under the soil, just starting to stir. Place a hand low on your belly and breathe into it. Notice any flicker of excitement or possibility.",
        "q": [
          "What new beginning can I sense?",
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
        "intro": "This is Key 32, Lasting Roots. Some things are worth tending slowly: relationships, skills, homes, dreams. What you nurture with care tends to endure.",
        "partner": "Every key has a partner, its other half. Yours is Key 42, Letting Life Unfold, which lets you build without gripping too tightly.",
        "try": "Rest both hands on a solid surface, a table or your knees. Feel its steadiness. Breathe, and think of one thing in your life you'd like to last.",
        "q": [
          "What deserves more of my patient care?",
          "What could I tend a little today?"
        ]
      },
      "42": {
        "intro": "This is Key 42, Letting Life Unfold. Not everything needs managing. Some things simply need time and trust, and the freedom to finish in their own way.",
        "partner": "Every key has a partner, its other half. Yours is Key 32, Lasting Roots, a reminder that letting go and taking care go hand in hand.",
        "try": "Take a full breath in. As you breathe out, let your hands fall open in your lap. Imagine putting something down that you don't need to carry right now.",
        "q": [
          "What am I trying to control?",
          "What might happen if I let it unfold?"
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
        "intro": "This is Key 40, Honoured No. Saying no isn't selfish. It's how you protect your energy, so that your yes can be wholehearted.",
        "partner": "Every key has a partner, its other half. Yours is Key 37, Full Cup: what your no makes possible, giving that doesn't drain you.",
        "try": "Sit tall and say a quiet, clear \"no\" out loud. Notice how it feels in your body. Then say \"yes\", and notice the difference. Both belong to you.",
        "q": [
          "What do I need to say no to?",
          "What would that make space for?"
        ]
      },
      "37": {
        "intro": "This is Key 37, Full Cup. Caring for others works best when you're cared for too. Relationships thrive when giving and receiving flow both ways.",
        "partner": "Every key has a partner, its other half. Yours is Key 40, Honoured No, which keeps your cup full by honouring your limits.",
        "try": "Imagine a cup inside your chest. Breathe in and picture it filling with warmth. Keep breathing until it feels full, then notice how it feels to have something to share.",
        "q": [
          "How full is my cup right now?",
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
        "intro": "This is Key 38, Heartfelt Courage. Some challenges ask us to keep going. When you fight for what you love rather than against what you fear, the struggle gains meaning.",
        "partner": "Every key has a partner, its other half. Yours is Key 39, Alive Energy: the spark that keeps you going.",
        "try": "Think of a challenge you're facing. Place a hand on your heart and ask, \"What do I love that this is for?\" Breathe that love into your chest.",
        "q": [
          "What makes this challenge worth meeting?"
        ]
      },
      "39": {
        "intro": "This is Key 39, Alive Energy. Restlessness and frustration are often creative energy looking for somewhere to go. Give it an outlet, and it comes alive.",
        "partner": "Every key has a partner, its other half. Yours is Key 38, Heartfelt Courage, which gives that energy a purpose worth pursuing.",
        "try": "Shake out your hands, then your arms and shoulders, for ten seconds. Stop, stand still and feel the buzz of energy in your body.",
        "q": [
          "Where is my energy wanting to go?",
          "What would I love to put it into?"
        ]
      }
    }
  },
  {
    "a": "51",
    "b": "57",
    "aff": {
      "51": "I have the courage to be who I am.",
      "57": "I trust the quiet knowing within me."
    },
    "lead": {
      "51": {
        "intro": "This is Key 51, Bold Steps. Being yourself sometimes means stepping out first, before anyone else does. Courage is the jolt of aliveness that moves you forward.",
        "partner": "Every key has a partner, its other half. Yours is Key 57, Quiet Knowing, which tells you which step is yours to take.",
        "try": "Stand or sit tall, and take a quick, bright breath in through your nose. Feel the little spark of energy it brings. Ask yourself, \"What's my next bold step?\"",
        "q": [
          "Where am I ready to show more of who I am?"
        ]
      },
      "57": {
        "intro": "This is Key 57, Quiet Knowing. Your intuition speaks softly, through a hunch, a feeling or a gentle nudge. The more you listen, the clearer it becomes.",
        "partner": "Every key has a partner, its other half. Yours is Key 51, Bold Steps, which gives you the courage to act on what you know.",
        "try": "Think of a choice in front of you. Turn it into a simple yes-or-no question, such as \"Is this right for me?\" or \"Do I want to go?\" Close your eyes, ask it silently, and notice the very first feeling in your body: an opening and lightness, or a tightening and heaviness. That first feeling is your knowing.",
        "q": [
          "If I already knew the answer, what would it be?",
          "What has that quiet whisper been nudging me towards?"
        ]
      }
    }
  },
  {
    "a": "52",
    "b": "58",
    "aff": {
      "52": "I grow at my own pace.",
      "58": "Joy rises in me naturally."
    },
    "lead": {
      "52": {
        "intro": "This is Key 52, Still Growth. Stillness holds power. When you move at your own pace, your energy gathers, and your growth becomes steady and strong.",
        "partner": "Every key has a partner, its other half. Yours is Key 58, Rising Joy: the joy that blossoms when you give yourself time.",
        "try": "Sit completely still for three slow breaths, like a mountain. Feel your weight settle downwards. Notice the calm strength in stillness.",
        "q": [
          "Where could I pause and let my energy gather?",
          "When the moment comes, where do I want it to go?"
        ]
      },
      "58": {
        "intro": "This is Key 58, Rising Joy. Joy is your natural state. It rises by itself when you make room for it, often in the smallest moments.",
        "partner": "Every key has a partner, its other half. Yours is Key 52, Still Growth, which lets that joy grow deep roots.",
        "try": "Think of something small that delights you: sunlight, a favourite song, a warm drink. Let a smile come. Feel where the joy rises in your body.",
        "q": [
          "What brings me joy that I could invite in more often?"
        ]
      }
    }
  },
  {
    "a": "53",
    "b": "54",
    "aff": {
      "53": "I trust what has already begun in me.",
      "54": "I rise, and I lift others with me."
    },
    "lead": {
      "53": {
        "intro": "This is Key 53, What's Already Begun. Something in you is already moving. Before the mind decides, the body often knows where it's being drawn. Trusting that pull, rather than hesitating, lets new beginnings unfold naturally.",
        "partner": "Every key has a partner, its other half. Yours is Key 54, Rising Together: the upward energy that grows from what's already begun.",
        "try": "Sit back and let your body relax completely, as if you're a passenger rather than the driver. Breathe slowly. Notice which way you feel gently pulled: towards a person, a place, an idea or a next step.",
        "q": [
          "What has already begun in me?",
          "Where would I go if I let my body lead?"
        ]
      },
      "54": {
        "intro": "This is Key 54, Rising Together. Your ambition is a good thing, especially when it lifts the people around you. Rising together makes the climb worth it.",
        "partner": "Every key has a partner, its other half. Yours is Key 53, What's Already Begun: the momentum already moving in you, ready to carry you upward.",
        "try": "Stand up and slowly raise your arms above your head as you breathe in. Feel yourself lengthen. As you lower them, imagine reaching a hand to someone beside you.",
        "q": [
          "What am I rising towards?",
          "Who could I bring with me?"
        ]
      }
    }
  },
  {
    "a": "55",
    "b": "59",
    "aff": {
      "55": "My spirit is free, whatever I am feeling.",
      "59": "Into me, I see, and I let others see me too."
    },
    "lead": {
      "55": {
        "intro": "This is Key 55, Free Spirit. Feelings come and go like weather. Underneath them all is a part of you that stays free, open and whole.",
        "partner": "Every key has a partner, its other half. Yours is Key 59, Being Seen: that freedom shared, the courage to be truly seen.",
        "try": "Imagine your feelings as clouds passing across a wide, open sky. Breathe slowly. Notice that you are the sky, spacious and free, whatever the weather.",
        "q": [
          "What would it feel like to let this feeling simply pass through?"
        ]
      },
      "59": {
        "intro": "This is Key 59, Being Seen. Closeness begins with seeing yourself honestly. When you're at home with who you are, you can let others in.",
        "partner": "Every key has a partner, its other half. Yours is Key 55, Free Spirit, which makes it safe to be seen, feelings and all.",
        "try": "Place a hand on your heart and close your eyes. Ask, \"What's true for me right now?\" Let the answer come, and meet it with warmth.",
        "q": [
          "Who or what would I like to let a little closer to my heart?",
          "What would that closeness feel like?"
        ]
      }
    }
  },
  {
    "a": "56",
    "b": "60",
    "aff": {
      "56": "My story enriches my life.",
      "60": "Structure gives my dreams a home."
    },
    "lead": {
      "56": {
        "intro": "This is Key 56, Rich Story. Every chapter of your life, the joyful and the challenging, adds richness and meaning. Your story is still being written.",
        "partner": "Every key has a partner, its other half. Yours is Key 60, Dream's Home, which gives your story a shape to grow in.",
        "try": "Think of one moment in your life that shaped who you are. Breathe in, and notice the gift it carries. Let yourself appreciate how far you've come.",
        "q": [
          "What chapter of my story am I in right now?",
          "What would I love the next one to hold?"
        ]
      },
      "60": {
        "intro": "This is Key 60, Dream's Home. Dreams need somewhere to land. A little structure, like a routine, a plan or a first step, turns inspiration into something real.",
        "partner": "Every key has a partner, its other half. Yours is Key 56, Rich Story, which keeps the structure full of life and meaning.",
        "try": "Picture a dream you hold. Now imagine building a simple, beautiful container for it, like a garden bed or a little house. Breathe, and notice how it feels to give it a home.",
        "q": [
          "What one simple routine or practical step would give my dream somewhere to land?"
        ]
      }
    }
  },
  {
    "a": "61",
    "b": "62",
    "aff": {
      "61": "I am inspired by the mystery of life.",
      "62": "I say what I mean, with love."
    },
    "lead": {
      "61": {
        "intro": "This is Key 61, Wonder. Wonder opens you to ideas and insights that come from beyond the thinking mind, and life is full of things to wonder at.",
        "partner": "Every key has a partner, its other half. Yours is Key 62, Clear Kindness, which helps you put your inspiration into words.",
        "try": "Look up at the sky, or out of a window, and let your gaze rest on the furthest thing you can see. Breathe slowly, and let a sense of wonder in.",
        "q": [
          "What in life fills me with wonder?"
        ]
      },
      "62": {
        "intro": "This is Key 62, Clear Kindness. Clear words are a kindness. When you say exactly what you mean, gently, people know where they stand.",
        "partner": "Every key has a partner, its other half. Yours is Key 61, Wonder, which gives your words a deeper source.",
        "try": "Think of something you'd like to say to someone. Shape it into one clear, kind sentence. Place a hand on your heart and say it softly to yourself.",
        "q": [
          "What would I love to say clearly and kindly?"
        ]
      }
    }
  },
  {
    "a": "63",
    "b": "64",
    "aff": {
      "63": "My questions open doors.",
      "64": "I trust the beauty of the unknown."
    },
    "lead": {
      "63": {
        "intro": "This is Key 63, Open Questions. A good question is a key. Curiosity leads you into new understanding and fresh possibilities.",
        "partner": "Every key has a partner, its other half. Yours is Key 64, Beautiful Unknown, which lets you enjoy the answers as they slowly arrive.",
        "try": "Take a breath and ask yourself a question beginning with \"I wonder…\" Say it slowly. Notice how your body feels when you're curious.",
        "q": [
          "What am I wondering about right now?"
        ]
      },
      "64": {
        "intro": "This is Key 64, Beautiful Unknown. The unknown is full of possibility. When you relax into it, your imagination comes alive with images, ideas and dreams.",
        "partner": "Every key has a partner, its other half. Yours is Key 63, Open Questions, which guides you gently through the unknown.",
        "try": "Close your eyes and imagine a mist slowly clearing. Let images, colours or shapes appear by themselves, in their own time.",
        "q": [
          "What did my imagination show me?"
        ]
      }
    }
  }
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
    <p>Some shifts come more easily with someone beside you. I'm Phoebe, of Radiant Oracle: a PSYCH-K® coach, Human Design coach, astrologer and tarot coach, and a long-time explorer of the Gene Keys. I work one to one and in groups, helping you change the beliefs that hold you back and read your own life more clearly.</p>
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
