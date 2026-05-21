def create_response(message, options=None, response_type="message", tips=None):

    return {
        "type": response_type,
        "message": message,
        "tips": tips or [],
        "options": options or []
    }
