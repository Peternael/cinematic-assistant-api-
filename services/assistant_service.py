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


def get_reply(choice: str):

    try:

        # حماية من None
        if choice is None:
            choice = ""

        # تنظيف النص
        choice = str(choice).strip().lower()

        # لو المستخدم كتب حاجة فاضية
        if choice == "":
            return {
                "type": "error",
                "message": "⚠️ اكتب وصف المشهد السينمائي أولاً",
                "options": [
                    {
                        "id": "start",
                        "title": "⬅️ الرئيسية"
                    }
                ]
            }

        # لو الاختيار موجود في الداتا
        if choice in assistant_data:
            return assistant_data[choice]

        # Smart AI cinematic fallback
        return {
            "type": "example",
            "message": (

                "🎬 AI Cinematic Prompt\n\n"

                "🇺🇸 English Prompt:\n\n"

                f"Two REAL Arabic male friends in a cinematic realistic scene about {choice}, "
                "ultra realistic atmosphere, cinematic lighting, "
                "slow natural movement, realistic skin texture, emotional acting, "
                "close-up cinematic camera shot, shallow depth of field, "
                "Hollywood movie realism, no crowd, no face distortion, "
                "high facial consistency, warm cinematic lighting.\n\n"

                "🇪🇬 Arabic Prompt:\n\n"

                f"مشهد سينمائي واقعي جدًا عن {choice}، "
                "إضاءة سينمائية احترافية، حركة طبيعية وبطيئة، "
                "تفاصيل واقعية جدًا للبشرة والوجه، "
                "الكاميرا قريبة بشكل سينمائي، "
                "مشهد فيلم حقيقي بجودة عالية."
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

        # بدل Server Error
        return {
            "type": "error",
            "message": f"❌ Backend Error:\n{str(e)}",
            "options": [
                {
                    "id": "start",
                    "title": "⬅️ الرئيسية"
                }
            ]
        }