from data.replies import assistant_data


def get_start_message():

    return assistant_data.get(
        "start",
        {
            "type": "start",
            "message": "🎬 مرحبًا بك في AI Cinematic Assistant",
            "options": []
        }
    )


def detect_scene_style(choice: str):

    text = choice.lower()

    style = {
        "scene_type": "cinematic realistic",
        "lighting": "warm cinematic lighting",
        "camera": "close-up cinematic camera shot",
        "atmosphere": "ultra realistic atmosphere",
        "movement": "slow natural movement",
    }

    # ROMANCE
    if (
        "حب" in text or
        "رومانسي" in text or
        "romantic" in text or
        "girlfriend" in text or
        "boyfriend" in text
    ):

        style["scene_type"] = "romantic cinematic"
        style["lighting"] = "soft romantic lighting"
        style["atmosphere"] = "emotional romantic atmosphere"

    # SAD
    elif (
        "حزين" in text or
        "sad" in text or
        "cry" in text or
        "بكاء" in text
    ):

        style["scene_type"] = "emotional dramatic cinematic"
        style["lighting"] = "dark emotional cinematic lighting"
        style["atmosphere"] = "sad emotional atmosphere"

    # ACTION
    elif (
        "اكشن" in text or
        "action" in text or
        "قتال" in text or
        "fight" in text
    ):

        style["scene_type"] = "high intensity action cinematic"
        style["camera"] = "dynamic cinematic tracking shot"
        style["movement"] = "fast realistic movement"

    # HORROR
    elif (
        "رعب" in text or
        "horror" in text or
        "مرعب" in text
    ):

        style["scene_type"] = "dark horror cinematic"
        style["lighting"] = "dark horror lighting"
        style["atmosphere"] = "terrifying cinematic atmosphere"

    # NILE / CAIRO
    if (
        "كورنيش" in text or
        "النيل" in text or
        "nile" in text or
        "cairo" in text
    ):

        style["lighting"] += ", Cairo night reflections"
        style["atmosphere"] += ", realistic Cairo nightlife"

    # RAIN
    if (
        "مطر" in text or
        "rain" in text
    ):

        style["atmosphere"] += ", rainy cinematic atmosphere"
        style["lighting"] += ", rain reflections"

    return style


def get_reply(choice: str):

    try:

        # حماية من None
        if choice is None:
            choice = ""

        # تنظيف النص
        choice = str(choice).strip()

        # لو المستخدم كتب حاجة فاضية
        if choice == "":

            return {
                "type": "error",

                "message":
                    "⚠️ اكتب وصف المشهد السينمائي أولاً",

                "options": [
                    {
                        "id": "start",
                        "title": "⬅️ الرئيسية"
                    }
                ]
            }

        # البحث في الردود الجاهزة
        lower_choice = choice.lower()

        if lower_choice in assistant_data:
            return assistant_data[lower_choice]

        # تحليل نوع المشهد
        style = detect_scene_style(choice)

        # إنشاء Prompt ذكي
        english_prompt = (

            f"Two REAL Arabic male friends in a "
            f"{style['scene_type']} scene about {choice}, "

            f"{style['atmosphere']}, "

            f"{style['lighting']}, "

            f"{style['movement']}, "

            "realistic skin texture, "
            "emotional realistic acting, "

            f"{style['camera']}, "

            "shallow depth of field, "
            "Hollywood cinematic realism, "
            "high facial consistency, "
            "no crowd, "
            "no face distortion, "
            "8k ultra realistic quality."
        )

        arabic_prompt = (

            f"مشهد سينمائي واقعي جدًا عن {choice}، "

            "إضاءة سينمائية احترافية، "
            "تفاصيل واقعية جدًا للبشرة والوجه، "
            "حركة طبيعية وواقعية، "
            "الكاميرا قريبة بشكل سينمائي، "
            "أجواء فيلم حقيقية بجودة عالية."
        )

        return {

            "type": "example",

            "message": (

                "🎬 AI Cinematic Prompt\n\n"

                "🇺🇸 English Prompt:\n\n"

                f"{english_prompt}\n\n"

                "🇪🇬 Arabic Prompt:\n\n"

                f"{arabic_prompt}"
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
        }

    except Exception as e:

        return {

            "type": "error",

            "message":
                f"❌ Backend Error:\n{str(e)}",

            "options": [

                {
                    "id": "start",
                    "title": "⬅️ الرئيسية"
                }
            ]
        }