assistant_data = {

    # ======================================================
    # START
    # ======================================================

    "start": {

        "type": "menu",

        "message": (

            "🎬 Welcome to AI Cinematic Studio\n\n"

            "أنا مساعدك السينمائي الذكي 🤖\n\n"

            "سأساعدك في إنشاء فيديوهات "
            "سينمائية واقعية بجودة احترافية.\n\n"

            "✨ يمكنك تعلم:\n"
            "🎥 كتابة Prompts احترافية\n"
            "🖼️ الحفاظ على الهوية\n"
            "🌧️ Cinematic Realism\n"
            "🎭 المشاهد العاطفية\n"
            "⚡ مشاهد الأكشن\n"
            "🌃 Cyberpunk Cairo\n\n"

            "اختر ما تريد 👇"
        ),

        "options": [

            {
                "id": "prompt_help",
                "title": "🎥 تعلم كتابة Prompt"
            },

            {
                "id": "upload_help",
                "title": "🖼️ رفع الصور"
            },

            {
                "id": "examples",
                "title": "💡 أمثلة سينمائية"
            },

            {
                "id": "mistakes",
                "title": "⚠️ الأخطاء الشائعة"
            },

            {
                "id": "pro_tips",
                "title": "🔥 نصائح احترافية"
            }
        ]
    },

    # ======================================================
    # PROMPT HELP
    # ======================================================

    "prompt_help": {

        "type": "tutorial",

        "message": (

            "🎥 لكي تكتب Prompt احترافي اذكر:\n\n"

            "📍 المكان\n"
            "🌙 الوقت\n"
            "💡 الإضاءة\n"
            "🎭 المشاعر\n"
            "📷 حركة الكاميرا\n"
            "🌧️ الجو العام\n"
            "👕 الملابس\n\n"

            "✨ كل وصف إضافي يعطي realism أعلى."
        ),

        "tips": [

            "استخدم cinematic lighting",
            "استخدم close-up shots",
            "استخدم emotional acting",
            "استخدم slow camera movement"
        ],

        "options": [

            {
                "id": "examples",
                "title": "💡 أمثلة جاهزة"
            },

            {
                "id": "start",
                "title": "⬅️ الرئيسية"
            }
        ]
    },

    # ======================================================
    # UPLOAD HELP
    # ======================================================

    "upload_help": {

        "type": "tutorial",

        "message": (

            "🖼️ رفع الصور مهم للحفاظ على الهوية.\n\n"

            "✅ استخدم صور واضحة\n"
            "✅ الوجه ظاهر بالكامل\n"
            "✅ إضاءة جيدة\n"
            "✅ تجنب الصور الضبابية\n"
            "✅ استخدم close-up face photos\n\n"

            "🎬 الصور الأفضل = نتائج أفضل."
        ),

        "options": [

            {
                "id": "examples",
                "title": "💡 أمثلة جاهزة"
            },

            {
                "id": "start",
                "title": "⬅️ الرئيسية"
            }
        ]
    },

    # ======================================================
    # EXAMPLES MENU
    # ======================================================

    "examples": {

        "type": "menu",

        "message": (

            "🎬 اختر نوع المشهد السينمائي 👇"
        ),

        "options": [

            {
                "id": "nile_walk",
                "title": "🌊 كورنيش النيل"
            },

            {
                "id": "romantic_cafe",
                "title": "❤️ كافيه رومانسي"
            },

            {
                "id": "rain_scene",
                "title": "🌧️ مشهد مطر"
            },

            {
                "id": "sad_scene",
                "title": "😢 مشهد حزين"
            },

            {
                "id": "wedding_scene",
                "title": "💍 مشهد خطوبة"
            },

            {
                "id": "action_scene",
                "title": "⚡ مشهد أكشن"
            },

            {
                "id": "cyberpunk_scene",
                "title": "🌃 Cyberpunk Cairo"
            },

            {
                "id": "metro_scene",
                "title": "🚇 مترو القاهرة"
            },

            {
                "id": "rooftop_scene",
                "title": "🏙️ سطح عمارة"
            },

            {
                "id": "sunset_scene",
                "title": "🌅 وقت الغروب"
            },

            {
                "id": "friends_laughing",
                "title": "😂 صحاب بيضحكوا"
            },

            {
                "id": "family_dinner",
                "title": "🍽️ عشاء عائلي"
            },

            {
                "id": "university_scene",
                "title": "🎓 جامعة"
            },

            {
                "id": "coffee_scene",
                "title": "☕ شرب القهوة"
            },

            {
                "id": "gym_scene",
                "title": "🏋️ الجيم"
            },

            {
                "id": "football_scene",
                "title": "⚽ كرة القدم"
            },

            {
                "id": "beach_scene",
                "title": "🏖️ البحر"
            },

            {
                "id": "hospital_scene",
                "title": "🏥 المستشفى"
            },

            {
                "id": "airport_scene",
                "title": "✈️ المطار"
            },

            {
                "id": "wedding_party_scene",
                "title": "🎉 فرح"
            }
        ]
    },

    # ======================================================
    # NILE WALK
    # ======================================================

    "nile_walk": {

        "type": "example",

        "message": (

            "🌊 Nile Corniche Walk\n\n"

            "🇺🇸 English Prompt:\n\n"

            "Two realistic Arabic young men walking together "
            "on the Nile Corniche at night in Cairo, cinematic "
            "street lighting, realistic skin texture, emotional "
            "atmosphere, slow cinematic camera movement.\n\n"

            "🇪🇬 Arabic Prompt:\n\n"

            "شابان عربيان يسيران معًا على كورنيش النيل "
            "ليلًا في القاهرة، إضاءة سينمائية دافئة، "
            "حركة كاميرا بطيئة."
        ),

        "options": [

            {
                "id": "examples",
                "title": "💡 كل الأمثلة"
            }
        ]
    },

    # ======================================================
    # ROMANTIC CAFE
    # ======================================================

    "romantic_cafe": {

        "type": "example",

        "message": (

            "❤️ Romantic Cafe Scene\n\n"

            "🇺🇸 English Prompt:\n\n"

            "A realistic Arabic couple sitting inside a luxurious "
            "quiet cafe at night, warm cinematic lighting, "
            "deep emotional eye contact, cinematic realism.\n\n"

            "🇪🇬 Arabic Prompt:\n\n"

            "شاب وفتاة عربيان يجلسان داخل مقهى فاخر "
            "هادئ ليلًا، إضاءة سينمائية دافئة."
        ),

        "options": [

            {
                "id": "examples",
                "title": "💡 كل الأمثلة"
            }
        ]
    },

    # ======================================================
    # RAIN SCENE
    # ======================================================

    "rain_scene": {

        "type": "example",

        "message": (

            "🌧️ Rain Drama Scene\n\n"

            "🇺🇸 English Prompt:\n\n"

            "A realistic Arabic man standing under heavy rain "
            "at night in Cairo, dramatic cinematic lighting, "
            "realistic wet skin texture.\n\n"

            "🇪🇬 Arabic Prompt:\n\n"

            "رجل عربي يقف تحت المطر الغزير "
            "ليلًا في القاهرة."
        ),

        "options": [

            {
                "id": "examples",
                "title": "💡 كل الأمثلة"
            }
        ]
    },

    # ======================================================
    # SAD SCENE
    # ======================================================

    "sad_scene": {

        "type": "example",

        "message": (

            "😢 Emotional Sad Scene\n\n"

            "🇺🇸 English Prompt:\n\n"

            "A realistic Arabic woman sitting alone during sunset, "
            "emotional cinematic lighting, realistic tears.\n\n"

            "🇪🇬 Arabic Prompt:\n\n"

            "فتاة عربية تجلس وحيدة وقت الغروب، "
            "إضاءة سينمائية حزينة."
        ),

        "options": [

            {
                "id": "examples",
                "title": "💡 كل الأمثلة"
            }
        ]
    },

    # ======================================================
    # WEDDING SCENE
    # ======================================================

    "wedding_scene": {

        "type": "example",

        "message": (

            "💍 Wedding Proposal Scene\n\n"

            "🇺🇸 English Prompt:\n\n"

            "A realistic Arabic man proposing to his girlfriend "
            "on a rooftop at night, cinematic city lights.\n\n"

            "🇪🇬 Arabic Prompt:\n\n"

            "شاب عربي يتقدم لخطبة حبيبته فوق سطح "
            "عمارة ليلًا."
        ),

        "options": [

            {
                "id": "examples",
                "title": "💡 كل الأمثلة"
            }
        ]
    },

    # ======================================================
    # ACTION SCENE
    # ======================================================

    "action_scene": {

        "type": "example",

        "message": (

            "⚡ Action Chase Scene\n\n"

            "🇺🇸 English Prompt:\n\n"

            "A realistic Arabic man running through dark rainy "
            "streets at night, handheld cinematic camera.\n\n"

            "🇪🇬 Arabic Prompt:\n\n"

            "رجل عربي يركض داخل شوارع مظلمة ممطرة "
            "ليلًا."
        ),

        "options": [

            {
                "id": "examples",
                "title": "💡 كل الأمثلة"
            }
        ]
    }
}