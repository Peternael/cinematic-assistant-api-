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
            "Two realistic Arabic young men walking together on the Nile Corniche at night in Cairo.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "شابان عربيان يسيران على كورنيش النيل ليلًا."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "romantic_cafe": {
        "type": "example",
        "message": (
            "❤️ Romantic Cafe Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic couple sitting inside luxury cafe at night.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "شاب وفتاة عربيان داخل كافيه فاخر."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "rain_scene": {
        "type": "example",
        "message": (
            "🌧️ Rain Drama Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic man standing under heavy rain at night.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "رجل عربي يقف تحت المطر ليلًا."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "sad_scene": {
        "type": "example",
        "message": (
            "😢 Emotional Sad Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic girl crying during sunset.\n\n"
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
            "Arabic man proposing to his girlfriend on rooftop.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "شاب عربي يتقدم لخطبة حبيبته."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "action_scene": {
        "type": "example",
        "message": (
            "⚡ Action Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic man running in dark rainy street.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "رجل عربي يركض في شارع مظلم."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "cyberpunk_scene": {
        "type": "example",
        "message": (
            "🌃 Cyberpunk Cairo\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Futuristic Cairo with neon cyberpunk lighting.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "القاهرة المستقبلية بإضاءة cyberpunk."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "metro_scene": {
        "type": "example",
        "message": (
            "🚇 Metro Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic young man standing in Cairo metro station.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "شاب عربي داخل محطة المترو."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "rooftop_scene": {
        "type": "example",
        "message": (
            "🏙️ Rooftop Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic friends talking on rooftop at night.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "أصدقاء عرب فوق سطح عمارة."
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
            "😂 Friends Laughing\n\n"
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
            "🍽️ Family Dinner\n\n"
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
            "Arabic student walking in university.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "طالب عربي داخل الجامعة."
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
            "رجل عربي يشرب القهوة."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "gym_scene": {
        "type": "example",
        "message": (
            "🏋️ Gym Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic young man training in gym.\n\n"
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
            "شاب وفتاة عربيان على البحر."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "hospital_scene": {
        "type": "example",
        "message": (
            "🏥 Hospital Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic man sitting alone in hospital corridor.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "رجل عربي داخل المستشفى."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "airport_scene": {
        "type": "example",
        "message": (
            "✈️ Airport Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic couple saying goodbye in airport.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "شاب وفتاة عربيان داخل المطار."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "wedding_party_scene": {
        "type": "example",
        "message": (
            "🎉 Wedding Party Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic wedding celebration with cinematic lights.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "حفل زفاف عربي."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "desert_scene": {
        "type": "example",
        "message": (
            "🏜️ Desert Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic man walking in desert during sunset.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "رجل عربي داخل الصحراء."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "gaming_scene": {
        "type": "example",
        "message": (
            "🎮 Gaming Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic gamer inside RGB gaming room.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "شاب عربي داخل غرفة Gaming."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "library_scene": {
        "type": "example",
        "message": (
            "📚 Library Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic student studying inside library.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "طالب عربي داخل المكتبة."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "restaurant_scene": {
        "type": "example",
        "message": (
            "🍕 Restaurant Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic family eating inside restaurant.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "عائلة عربية داخل مطعم."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "mall_scene": {
        "type": "example",
        "message": (
            "🛍️ Mall Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic couple walking inside mall.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "شاب وفتاة داخل المول."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "boxing_scene": {
        "type": "example",
        "message": (
            "🥊 Boxing Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic boxer training in boxing gym.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "ملاكم عربي داخل الجيم."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "street_food_scene": {
        "type": "example",
        "message": (
            "🌮 Street Food Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic young man eating street food at night.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "شاب عربي يأكل street food."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "train_scene": {
        "type": "example",
        "message": (
            "🚆 Train Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic man sitting near train window.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "رجل عربي داخل القطار."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "exam_scene": {
        "type": "example",
        "message": (
            "📝 Exam Scene\n\n"
            "🇺🇸 English Prompt:\n\n"
            "Arabic student studying before exams.\n\n"
            "🇪🇬 Arabic Prompt:\n\n"
            "طالب عربي يذاكر قبل الامتحانات."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
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

            {"id": "start", "title": "⬅️ الرئيسية"}

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
            "✅ استخدم realistic atmosphere"
        ),

        "options": [

            {"id": "start", "title": "⬅️ الرئيسية"}

        ]
    }

}