from data.replies import assistant_data


def get_start_message():
    return assistant_data["start"]



def get_reply(choice: str):

    if choice not in assistant_data:

        return {
            "type": "error",
            "message": "لم أفهم اختيارك.",
            "options": [
                {
                    "id": "start",
                    "title": "⬅️ الرئيسية"
                }
            ]
        }

    return assistant_data[choice]
