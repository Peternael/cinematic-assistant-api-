assistant_data = {

    # ======================================================
    # START
    # ======================================================

    "start": {

        "type": "menu",

        "message": (

            "👋 أهلاً بك في AI Cinematic Studio\n\n"

            "أنا مساعدك السينمائي 🤖\n\n"

            "مهمتي مساعدتك في إنشاء فيديوهات "
            "سينمائية واقعية بجودة احترافية.\n\n"

            "✨ سأساعدك في:\n"
            "🎥 كتابة Prompts احترافية\n"
            "🖼️ الحفاظ على الهوية\n"
            "🎭 بناء المشاهد العاطفية\n"
            "🌧️ إنشاء cinematic realism\n"
            "⚡ تحسين جودة الفيديو\n\n"

            "اختر ما تريد تعلمه 👇"
        ),

        "options": [

            {
                "id": "prompt_help",
                "title": "🎥 كيف أكتب Prompt؟"
            },

            {
                "id": "upload_help",
                "title": "🖼️ كيف أرفع الصور؟"
            },

            {
                "id": "examples",
                "title": "💡 أمثلة جاهزة"
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

            "🎥 كتابة الـ Prompt هي أهم خطوة.\n\n"

            "لكي تحصل على فيديو سينمائي احترافي اذكر:\n\n"

            "📍 المكان\n"
            "🌙 الوقت\n"
            "💡 الإضاءة\n"
            "🎭 المشاعر\n"
            "📷 حركة الكاميرا\n"
            "🌧️ الجو العام\n"
            "👕 الملابس\n\n"

            "✨ كل وصف إضافي يساعد Veo "
            "على إنتاج مشهد أكثر واقعية."
        ),

        "tips": [

            "استخدم cinematic lighting",
            "استخدم close-up shots",
            "استخدم slow camera movement",
            "استخدم emotional acting"
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
            "✅ الوجه يكون ظاهر بالكامل\n"
            "✅ إضاءة جيدة\n"
            "✅ صورة قريبة للوجه\n"
            "✅ تجنب الصور الضبابية\n\n"

            "🎬 كلما كانت الصور أوضح "
            "كلما كانت النتيجة أكثر واقعية."
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
    # EXAMPLES
    # ======================================================

    "examples": {

        "type": "menu",

        "message": (

            "🎬 اختر نوع المشهد السينمائي 👇"
        ),

        "options": [

            {
                "id": "romance_example",
                "title": "❤️ مشهد رومانسي"
            },

            {
                "id": "rain_example",
                "title": "🌧️ مشهد مطر"
            },

            {
                "id": "action_example",
                "title": "⚡ مشهد أكشن"
            },

            {
                "id": "cyberpunk_example",
                "title": "🌃 Cyberpunk Cairo"
            },

            {
                "id": "start",
                "title": "⬅️ الرئيسية"
            }
        ]
    },

    # ======================================================
    # ROMANCE
    # ======================================================

    "romance_example": {

        "type": "example",

        "message": (

            "❤️ Prompt رومانسي احترافي\n\n"

            "شاب وفتاة عربيان يجلسان داخل "
            "مقهى فاخر هادئ ليلًا، "
            "إضاءة سينمائية دافئة، "
            "حركة كاميرا بطيئة، "
            "تعبيرات وجه عاطفية، "
            "cinematic realism, "
            "realistic skin texture."
        ),

        "options": [

            {
                "id": "rain_example",
                "title": "🌧️ مشهد مطر"
            },

            {
                "id": "start",
                "title": "⬅️ الرئيسية"
            }
        ]
    },

    # ======================================================
    # RAIN
    # ======================================================

    "rain_example": {

        "type": "example",

        "message": (

            "🌧️ Prompt مطر سينمائي\n\n"

            "رجل عربي يقف تحت المطر ليلًا "
            "في القاهرة، cinematic lighting، "
            "slow motion، realistic wet skin، "
            "dramatic atmosphere."
        ),

        "options": [

            {
                "id": "action_example",
                "title": "⚡ مشهد أكشن"
            },

            {
                "id": "start",
                "title": "⬅️ الرئيسية"
            }
        ]
    },

    # ======================================================
    # ACTION
    # ======================================================

    "action_example": {

        "type": "example",

        "message": (

            "⚡ Prompt أكشن احترافي\n\n"

            "رجل عربي يركض داخل شوارع "
            "ممطرة مظلمة، handheld camera، "
            "dramatic cinematic lighting، "
            "realistic body movement."
        ),

        "options": [

            {
                "id": "cyberpunk_example",
                "title": "🌃 Cyberpunk Cairo"
            },

            {
                "id": "start",
                "title": "⬅️ الرئيسية"
            }
        ]
    },

    # ======================================================
    # CYBERPUNK
    # ======================================================

    "cyberpunk_example": {

        "type": "example",

        "message": (

            "🌃 Cyberpunk Cairo\n\n"

            "رجل عربي يسير داخل شوارع "
            "القاهرة المستقبلية بإضاءة neon، "
            "cinematic reflections، "
            "slow tracking shot، "
            "ultra realistic atmosphere."
        ),

        "options": [

            {
                "id": "examples",
                "title": "💡 كل الأمثلة"
            },

            {
                "id": "start",
                "title": "⬅️ الرئيسية"
            }
        ]
    },

    # ======================================================
    # MISTAKES
    # ======================================================

    "mistakes": {

        "type": "warning",

        "message": (

            "⚠️ أخطاء تقلل جودة الفيديو:\n\n"

            "🚫 prompts قصيرة جدًا\n"
            "🚫 صور ضبابية\n"
            "🚫 كثرة الشخصيات\n"
            "🚫 حركة عنيفة جدًا\n"
            "🚫 crowd scenes\n"
            "🚫 fast camera movement"
        ),

        "options": [

            {
                "id": "prompt_help",
                "title": "🎥 تعلم كتابة Prompt"
            },

            {
                "id": "start",
                "title": "⬅️ الرئيسية"
            }
        ]
    },

    # ======================================================
    # PRO TIPS
    # ======================================================

    "pro_tips": {

        "type": "tips",

        "message": (

            "🔥 نصائح احترافية:\n\n"

            "✅ استخدم close-up shots\n"
            "✅ استخدم cinematic lighting\n"
            "✅ استخدم emotional acting\n"
            "✅ استخدم slow movement\n"
            "✅ اجعل المشهد بسيط وواضح\n"
            "✅ استخدم realistic atmosphere"
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
    }
}