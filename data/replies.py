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

            {"id": "prompt_help", "title": "🎥 تعلم كتابة Prompt"},
            {"id": "upload_help", "title": "🖼️ رفع الصور"},
            {"id": "examples", "title": "💡 أمثلة سينمائية"},
            {"id": "mistakes", "title": "⚠️ الأخطاء الشائعة"},
            {"id": "pro_tips", "title": "🔥 نصائح احترافية"}

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

            {"id": "examples", "title": "💡 أمثلة جاهزة"},
            {"id": "start", "title": "⬅️ الرئيسية"}

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

            {"id": "examples", "title": "💡 أمثلة جاهزة"},
            {"id": "start", "title": "⬅️ الرئيسية"}

        ]
    },

    # ======================================================
    # EXAMPLES MENU
    # ======================================================

    "examples": {

        "type": "menu",

        "message": "🎬 اختر نوع المشهد السينمائي 👇",

        "options": [

            {"id": "nile_walk", "title": "🌊 كورنيش النيل"},
            {"id": "romantic_cafe", "title": "❤️ كافيه رومانسي"},
            {"id": "rain_scene", "title": "🌧️ مشهد مطر"},
            {"id": "sad_scene", "title": "😢 مشهد حزين"},
            {"id": "wedding_scene", "title": "💍 مشهد خطوبة"},
            {"id": "action_scene", "title": "⚡ مشهد أكشن"},
            {"id": "cyberpunk_scene", "title": "🌃 Cyberpunk Cairo"},
            {"id": "metro_scene", "title": "🚇 مترو القاهرة"},
            {"id": "rooftop_scene", "title": "🏙️ سطح عمارة"},
            {"id": "sunset_scene", "title": "🌅 وقت الغروب"},
            {"id": "friends_laughing", "title": "😂 صحاب بيضحكوا"},
            {"id": "family_dinner", "title": "🍽️ عشاء عائلي"},
            {"id": "university_scene", "title": "🎓 جامعة"},
            {"id": "coffee_scene", "title": "☕ شرب القهوة"},
            {"id": "gym_scene", "title": "🏋️ الجيم"},
            {"id": "football_scene", "title": "⚽ كرة القدم"},
            {"id": "beach_scene", "title": "🏖️ البحر"},
            {"id": "hospital_scene", "title": "🏥 المستشفى"},
            {"id": "airport_scene", "title": "✈️ المطار"},
            {"id": "wedding_party_scene", "title": "🎉 فرح"},
            {"id": "night_drive_scene", "title": "🚘 Night Drive"},
            {"id": "desert_scene", "title": "🏜️ الصحراء"},
            {"id": "gaming_scene", "title": "🎮 Gaming"},
            {"id": "library_scene", "title": "📚 المكتبة"},
            {"id": "restaurant_scene", "title": "🍕 مطعم"},
            {"id": "mall_scene", "title": "🛍️ المول"},
            {"id": "boxing_scene", "title": "🥊 Boxing"},
            {"id": "street_food_scene", "title": "🌮 Street Food"},
            {"id": "train_scene", "title": "🚆 القطار"},
            {"id": "exam_scene", "title": "📝 الامتحانات"}

        ]
    },

    # ======================================================
    # SCENES
    # ======================================================

    "nile_walk": {
        "type": "example",
        "message": (
            "🌊 Nile Corniche Walk\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Two realistic Arabic young men walking together "
            "on the Nile Corniche at night in Cairo, cinematic "
            "street lighting, emotional atmosphere.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "شابان عربيان يسيران معًا على كورنيش النيل ليلًا."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "romantic_cafe": {
        "type": "example",
        "message": (
            "❤️ Romantic Cafe Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "A realistic Arabic couple sitting inside a luxurious "
            "quiet cafe at night, warm cinematic lighting.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "شاب وفتاة عربيان يجلسان داخل مقهى فاخر ليلًا."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "rain_scene": {
        "type": "example",
        "message": (
            "🌧️ Rain Drama Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "A realistic Arabic man standing under heavy rain "
            "at night in Cairo.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "رجل عربي يقف تحت المطر الغزير ليلًا."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "sad_scene": {
        "type": "example",
        "message": (
            "😢 Emotional Sad Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "A realistic Arabic woman crying during sunset.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "فتاة عربية تبكي وقت الغروب."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "wedding_scene": {
        "type": "example",
        "message": (
            "💍 Wedding Proposal Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "A realistic Arabic man proposing on rooftop.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "شاب عربي يتقدم لخطبة حبيبته."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "action_scene": {
        "type": "example",
        "message": (
            "⚡ Action Chase Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "A realistic Arabic man running through rainy streets.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "رجل عربي يركض داخل شوارع ممطرة."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "cyberpunk_scene": {
        "type": "example",
        "message": (
            "🌃 Cyberpunk Cairo\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Futuristic cyberpunk Cairo streets with neon lights.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "شوارع القاهرة المستقبلية بإضاءة neon."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "metro_scene": {
        "type": "example",
        "message": (
            "🚇 Cairo Metro Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic man standing inside Cairo metro station.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "شاب عربي يقف داخل محطة مترو القاهرة."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "rooftop_scene": {
        "type": "example",
        "message": (
            "🏙️ Rooftop Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic friends sitting together on rooftop at night.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "شابان عربيان يجلسان فوق سطح عمارة."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "sunset_scene": {
        "type": "example",
        "message": (
            "🌅 Sunset Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic girl walking during sunset.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "فتاة عربية تسير وقت الغروب."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "friends_laughing": {
        "type": "example",
        "message": (
            "😂 Friends Laughing Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic friends laughing together inside cafe.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "أصدقاء عرب يضحكون داخل كافيه."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "family_dinner": {
        "type": "example",
        "message": (
            "🍽️ Family Dinner Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic family having dinner together.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "عائلة عربية تتناول العشاء."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "university_scene": {
        "type": "example",
        "message": (
            "🎓 University Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic student walking in university campus.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "طالب عربي يسير داخل الجامعة."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "coffee_scene": {
        "type": "example",
        "message": (
            "☕ Coffee Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic man drinking coffee alone.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "رجل عربي يشرب القهوة وحده."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "gym_scene": {
        "type": "example",
        "message": (
            "🏋️ Gym Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic young man training inside gym.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "شاب عربي يتمرن داخل الجيم."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "football_scene": {
        "type": "example",
        "message": (
            "⚽ Football Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic football player inside stadium.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "لاعب كرة قدم عربي داخل الملعب."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "beach_scene": {
        "type": "example",
        "message": (
            "🏖️ Beach Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic couple walking on beach during sunset.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "شاب وفتاة عربيان يسيران على البحر."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "hospital_scene": {
        "type": "example",
        "message": (
            "🏥 Hospital Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic man sitting alone inside hospital corridor.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "رجل عربي يجلس داخل ممر مستشفى."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "airport_scene": {
        "type": "example",
        "message": (
            "✈️ Airport Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic couple saying goodbye at airport.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "شاب وفتاة عربيان يودعان بعضهما."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "wedding_party_scene": {
        "type": "example",
        "message": (
            "🎉 Wedding Party Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic wedding celebration with cinematic lighting.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "حفل زفاف عربي بإضاءة سينمائية."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    }

}