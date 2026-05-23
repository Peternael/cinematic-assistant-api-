from data.replies import assistant_data


def get_start_message():
    return assistant_data["start"]


def get_reply(choice: str):

    # تنظيف النص
    choice = choice.strip().lower()

    # لو الاختيار موجود
    if choice in assistant_data:
        return assistant_data[choice]

    # Smart fallback
    return {
        "type": "example",
        "message": (

            "🎬 AI Cinematic Prompt\n\n"

            "🇺🇸 English Prompt:\n\n"

            f"A realistic cinematic scene about {choice}, "
            "ultra realistic atmosphere, cinematic lighting, "
            "slow movement, realistic skin texture, emotional acting, "
            "close-up cinematic camera shot, no crowd, "
            "high quality movie scene.\n\n"

            "🇪🇬 Arabic Prompt:\n\n"

            f"مشهد سينمائي واقعي عن {choice}، "
            "إضاءة سينمائية احترافية، حركة بطيئة وطبيعية، "
            "تفاصيل واقعية جدًا، الكاميرا قريبة بشكل سينمائي، "
            "أجواء فيلم حقيقية."
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