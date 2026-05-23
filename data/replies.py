assistant_data = {
    # ======================================================
    # START
    # ======================================================
    "start": {
        "type": "menu",
        "message": (
            "🎬 Welcome to AI Cinematic Studio\n\n"
            "أنا مساعدك السينمائي الذكي 🤖\n\n"
            "سأساعدك في إنشاء فيديوهات سينمائية واقعية بجودة احترافية.\n\n"
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
    # SCENES (UPDATED TO CINEMATIC REALISM)
    # ======================================================
    "nile_walk": {
        "type": "example",
        "message": (
            "🌊 Nile Corniche Walk\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic close-up shot of two realistic Arabic young men walking together on the Nile Corniche in Cairo during sunset. They are talking and laughing softly. Warm, soft golden hour lighting, cinematic atmosphere, hyper-realistic, extremely slow and subtle camera movement, empty background with no other people.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "ولدين ماشيين جنب بعض على كورنيش النيل وقت الغروب، بيتكلموا وبيضحكوا بهدوء، حركة بسيطة وبطيئة جدًا، الكاميرا قريبة منهم بشكل سينمائي، إضاءة الغروب دافئة وناعمة، مشهد واقعي جدًا، بدون أي أشخاص آخرين في الخلفية."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "romantic_cafe": {
        "type": "example",
        "message": (
            "❤️ Romantic Cafe Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic medium close-up of an Arabic young man and woman sitting across from each other inside a luxury cozy cafe at night. Soft candlelight illuminating their faces, emotional acting, romantic eye contact, warm cinematic lighting, shallow depth of field, slow panning camera movement, realistic textures.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "شاب وفتاة عربيان يجلسان متقابلين داخل كافيه فاخر ودافئ ليلًا، نظرات عاطفية متبادلة، إضاءة شموع خافتة وناعمة على وجوههم، الكاميرا تتحرك ببطء شديد، عزل سينمائي للخلفية، مشهد رومانسي واقعي بجودة عالية."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "rain_scene": {
        "type": "example",
        "message": (
            "🌧️ Rain Drama Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic close-up shot of a handsome Arabic man standing alone under heavy rain at night on a dark city street. Water droplets running down his face, deep emotional look, moody dramatic neon lighting reflecting on the wet ground, slow push-in camera movement, cinematic realism, 4k resolution.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "رجل عربي وسيم يقف بمفرده تحت مطر غزير ليلًا في شارع مظلم، قطرات الماء تتساقط على وجهه، ملامح عاطفية عميقة، إضاءة نيون درامية تنعكس على الأرض المبللة، الكاميرا تقترب منه ببطء شديد، مشهد سينمائي واقعي للغاية."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "sad_scene": {
        "type": "example",
        "message": (
            "😢 Emotional Sad Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic tight close-up of a beautiful Arabic girl crying silently during sunset. Tears rolling down her cheek, profound sad emotional expression, soft warm cinematic lighting blending with the sunset glow, shallow depth of field, extremely subtle and slow camera panning, hyper-detailed.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "لقطة قريبة جداً لفتاة عربية تبكي بصمت وقت الغروب، الدموع تسيل على خدها، ملامح حزن عميقة ومؤثرة، إضاءة الغروب الدافئة والناعمة مدمجة في المشهد، عزل تام للخلفية، حركة كاميرا بطيئة وهادئة للغاية."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "wedding_scene": {
        "type": "example",
        "message": (
            "💍 Wedding Proposal Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic medium shot of an Arabic young man proposing to his beautiful girlfriend on a decorated rooftop overlooking the city at night. He is holding an engagement ring box, emotional reactions, warm fairy lights background, cinematic lighting, slow circular camera movement, cinematic realism.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "شاب عربي يتقدم لخطبة حبيبته فوق سطح عمارة مزين ومطل على المدينة ليلًا، يمسك علبة خاتم الخطوبة، ملامح الفرحة والصدمة العاطفية واضحة، إضاءة دافئة من حبال النور في الخلفية، حركة كاميرا دائرية بطيئة وسينمائية."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "action_scene": {
        "type": "example",
        "message": (
            "⚡ Action Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic intense medium shot of an Arabic man running with determination through a dark, wet, rainy narrow street at night. Dramatic low-key lighting, heavy rain atmosphere, tracking camera shot following his motion smoothly, detailed wet clothing, cinematic realism, dark moody color grading.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "رجل عربي يركض بإصرار وعزيمة في شارع ضيق ومظلم ومبلل بالمطر ليلًا، إضاءة درامية خافتة، أجواء مطر غزير، الكاميرا تتبعه بسلاسة وبدون اهتزاز عنيف، تفاصيل ملابسه المبتلة واضحة، ألوان سينمائية داكنة."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "cyberpunk_scene": {
        "type": "example",
        "message": (
            "🌃 Cyberpunk Cairo\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic wide shot of futuristic Cairo city streets with a cyberpunk aesthetic at night. Neon signs in Arabic glowing in pink and cyan, flying vehicles cruising between old and futuristic buildings, misty and rainy atmosphere, cinematic lighting, slow establishing drone camera movement, hyper-realistic sci-fi.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "لقطة واسعة لمدينة القاهرة المستقبلية بأجواء وجاذبية الـ Cyberpunk ليلًا، لوحات نيون باللغة العربية تضيء باللون البينك والسيان، مركبات طائرة بين المباني القديمة والحديثة، أجواء ضبابية وممطرة، حركة كاميرا بطيئة وسينمائية."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "metro_scene": {
        "type": "example",
        "message": (
            "🚇 Metro Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic close-up of a young Arabic man standing inside Cairo metro station, looking thoughtful as the train approaches. Flickering station lights, cinematic lighting, shallow depth of field, motion blur of the passing train in the background, slow camera pan, hyper-realistic environment.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "لقطة قريبة لشاب عربي يقف داخل محطة مترو القاهرة، ملامحه تبدو غارقة في التفكير مع اقتراب القطار، إضاءة المحطة السينمائية، عزل قوي للخلفية مع ظهور حركة القطار السريعة بـ Motion Blur، حركة كاميرا بطيئة وواقعية."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "rooftop_scene": {
        "type": "example",
        "message": (
            "🏙️ Rooftop Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic medium shot of a group of young Arabic friends sitting on a cozy rooftop in Cairo at night, chatting and laughing happily. Warm ambient lighting, city lights glowing softly in the distant background, slow cinematic panning shot, clear dark night sky, hyper-realistic, natural acting.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "مجموعة من الأصدقاء الشباب العرب يجلسون فوق سطح عمارة دافئ في القاهرة ليلًا، يتحدثون ويضحكون بسعادة، إضاءة محيطة دافئة، أضواء المدينة تلمع بنعومة في الخلفية البعيدة، حركة كاميرا بطيئة وسينمائية، تمثيل طبيعي وواقعي."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "sunset_scene": {
        "type": "example",
        "message": (
            "🌅 Sunset Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic close-up profile shot of a beautiful Arabic girl walking peacefully during golden hour sunset. Beautiful golden sunlight catching her hair, calm facial expression, soft backlit cinematic lighting, shallow depth of field, slow tracking camera movement side-by-side, hyper-realistic.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "لقطة جانبية قريبة لفتاة عربية تسير بهدوء وقت غروب الشمس، أشعة الشمس الذهبية تتخلل شعرها، ملامح وجه هادئة، إضاءة خلفية دافئة وناعمة، عزل تام للخلفية، الكاميرا تتابعها من الجانب ببطء شديد، مشهد واقعي مذهل."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "friends_laughing": {
        "type": "example",
        "message": (
            "😂 Friends Laughing\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic medium close-up of young Arabic friends laughing genuinely together inside a modern cafe. Authentic emotional expressions, cozy cinematic lighting, detailed facial textures, shallow depth of field, slow and smooth camera movement, hyper-realistic candid moment.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "لقطة قريبة لمجموعة من الأصدقاء الشباب العرب يضحكون من قلبهم معًا داخل كافيه مودرن، تعبيرات وجه عفوية وحقيقية، إضاءة سينمائية دافئة ومريحة، عزل قوي للخلفية، حركة كاميرا ناعمة وبطيئة جدًا، مشهد واقعي وعفوي."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "family_dinner": {
        "type": "example",
        "message": (
            "🍽️ Family Dinner\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic medium shot of a happy Arabic family having dinner together at a richly decorated dining table. Warm interior cinematic lighting, smiling faces, authentic expressions of sharing food, slow and smooth camera panning, detailed textures of Egyptian food, hyper-realistic home environment.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "عائلة عربية سعيدة تتناول وجبة العشاء معًا حول طاولة طعام غنية، إضاءة داخلية دافئة وسينمائية، وجوه مبتسمة وتعبيرات حقيقية أثناء مشاركة الطعام، الكاميرا تتحرك بسلاسة وبطء، تفاصيل الأكل المصري واضحة، أجواء منزلية واقعية."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "university_scene": {
        "type": "example",
        "message": (
            "🎓 University Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic medium close-up of an Arabic student walking through a sunny university campus courtyard, carrying books. Bright natural daylight, soft shadows, green trees in the background, confident smile, slow tracking camera shot moving backwards ahead of him, cinematic realism.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "طالب عربي يسير في ساحة الجامعة المشمسة وهو يحمل كتبًا، إضاءة نهارية طبيعية ومشرقة، ظلال ناعمة، أشجار خضراء في الخلفية، ابتسامة واثقة، الكاميرا تتحرك للخلف ببطء أمامه لتتابعه بشكل سينمائي واقعي."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "coffee_scene": {
        "type": "example",
        "message": (
            "☕ Coffee Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic close-up of a thoughtful Arabic man slowly drinking hot coffee alone next to a rainy window inside a quiet cafe. Steam rising from the coffee cup, soft moody cinematic lighting, rain droplets visible on the glass window, slow push-in camera movement, detailed and realistic.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "لقطة قريبة لرجل عربي غارق في أفكاره يشرب القهوة الساخنة بمفرده بجانب نافذة ممطرة داخل كافيه هادئ، البخار يتصاعد من فنجان القهوة، إضاءة درامية ناعمة، قطرات المطر تظهر على الزجاج، الكاميرا تقترب ببطء شديد."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "gym_scene": {
        "type": "example",
        "message": (
            "🏋️ Gym Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic intense medium close-up of a muscular Arabic young man training hard inside a dark gym. Sweat dripping from his face, focused and determined expression, dramatic overhead spot lighting, detailed muscle textures, slow tracking camera movement, raw cinematic realism.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "شاب عربي مفتول العضلات يتمرن بقوة واحترافية داخل جيم مظلم، حبات العرق تتساقط من وجهه، ملامح تركيز وإصرار شديد، إضاءة درامية مركزة من الأعلى، تفاصيل العضلات واضحة، حركة كاميرا بطيئة ومتابعة للمشهد بواقعية."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "football_scene": {
        "type": "example",
        "message": (
            "⚽ Football Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic medium shot of an Arabic football player standing inside a huge stadium under bright stadium floodlights. Focused intense expression, grass field details, dynamic dramatic lighting, subtle camera rotation around him, cinematic realism, sportswear details clear.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "لاعب كرة قدم عربي يقف بتركيز داخل ملعب ضخم تحت إضاءة الكشافات القوية، تعبيرات وجه حادة ومليئة بالتحدي، تفاصيل عشب الملعب واضحة، إضاءة ديناميكية درامية، حركة كاميرا دائرية خفيفة وبطيئة حول اللاعب، مشهد سينمائي واقعي."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "beach_scene": {
        "type": "example",
        "message": (
            "🏖️ Beach Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic wide medium shot of an Arabic couple walking peacefully on a sandy beach during a beautiful sunset. Gentle sea waves, soft warm golden hour lighting reflecting on the water, calm and happy expressions, slow lateral tracking camera movement, hyper-realistic, cinematic atmosphere.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "شاب وفتاة عربيان يسيران بهدوء على شاطئ البحر وقت الغروب الساحر، أمواج البحر هادئة، إضاءة الغروب الدافئة تنعكس على المياة، ملامح هادئة وسعيدة، الكاميرا تتابعهما من الجانب ببطء وسلاسة، أجواء سينمائية واقعية جدًا."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "hospital_scene": {
        "type": "example",
        "message": (
            "🏥 Hospital Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic cold medium shot of an Arabic man sitting alone in a quiet hospital corridor, looking worried and anxious. Soft clean overhead lighting, cool color grading, realistic hospital environment, shallow depth of field, slow zoom-in camera movement, emotional acting, dramatic atmosphere.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "رجل عربي يجلس بمفرده في ممر مستشفى هادئ، ملامحه قلقة ومليئة بالخوف والترقب، إضاءة علوية بيضاء ونظيفة، ألوان باردة ودرامية للمشهد، عزل سينمائي للممر، زووم بطيء جدًا بالكاميرا نحو الرجل لتوضيح مشاعره بواقعية."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "airport_scene": {
        "type": "example",
        "message": (
            "✈️ Airport Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic emotional medium shot of an Arabic couple saying goodbye to each other inside a modern airport terminal. Emotional faces, luggage next to them, soft cinematic lighting through large windows, slow camera panning, shallow depth of field, realistic cinematic atmosphere.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "شاب وفتاة عربيان يودعان بعضهما بملامح عاطفية متأثرة داخل صالة مطار حديثة، الحقائب بجانبهما، إضاءة سينمائية ناعمة قادمة من النوافذ الكبيرة، حركة كاميرا بطيئة وناعمة، عزل سينمائي يركز على مشاعرهما بواقعية."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "wedding_party_scene": {
        "type": "example",
        "message": (
            "🎉 Wedding Party Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic dynamic shot of an Arabic bride and groom dancing together happily during their wedding celebration. Luxury ballroom, beautiful cinematic lights and sparks in background, joyous emotional acting, slow moving camera circling the couple smoothly, hyper-realistic details.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "عريس وعروسة عربيان يرقصان معًا بسعادة غامرة داخل قاعة زفاف فاخرة، إضاءة سينمائية مبهجة مع تأثيرات إضاءة وشرار ناعم في الخلفية، تعبيرات فرحة حقيقية، حركة كاميرا دائرية بطيئة وانسيابية حولهما، تفاصيل واقعية واحترافية."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "desert_scene": {
        "type": "example",
        "message": (
            "🏜️ Desert Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic wide establishing shot of an Arabic man walking alone across vast desert sand dunes during a dramatic sunset. Golden hour sun low on the horizon, rich orange and red sky, soft wind blowing sand ripples, slow majestic camera drone movement, high-end realism.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "لقطة واسعة وسينمائية لرجل عربي يسير بمفرده وسط كثبان رملية صحراوية شاسعة وقت الغروب الدرامي، الشمس منخفضة في الأفق، السماء غنية بألوان البرتقالي والأحمر، رياح خفيفة تحرك الرمل، حركة كاميرا طائرة بطيئة وماجستيك، واقعية فائقة."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "gaming_scene": {
        "type": "example",
        "message": (
            "🎮 Gaming Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic close-up of a focused Arabic young gamer sitting inside a dark room illuminated by colorful RGB gaming lights. Intense focused expression reflecting on his face from the screen, premium headphones on, slow slide camera movement, realistic skin textures, high-quality cinematic look.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "لقطة قريبة لشاب عربي مأخوذ بالتركيز الشديد أثناء اللعب داخل غرفة مظلمة تضيئها أنوار RGB الملونة، إضاءة الشاشة تنعكس على وجهه بدقة، يرتدي سماعات جيمنج احترافية، حركة كاميرا جانبية بطيئة وناعمة، تفاصيل واقعية جداً للبشرة."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "library_scene": {
        "type": "example",
        "message": (
            "📚 Library Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic medium close-up of an Arabic student studying carefully inside a majestic old library. Stacks of wooden bookshelves filled with books in the background, soft warm lighting focused on the desk, thoughtful facial expression, slow push-in camera movement, cinematic realism.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "طالب عربي يذاكر بتركيز وعناية داخل مكتبة قديمة وعريقة، صفوف من الرفوف الخشبية المليئة بالكتب في الخلفية، إضاءة دافئة وناعمة مركزة على المكتب، ملامح وجه مستغرقة في القراءة، حركة كاميرا تقترب ببطء شديد، مشهد واقعي هادئ."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "restaurant_scene": {
        "type": "example",
        "message": (
            "🍕 Restaurant Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic medium shot of an Arabic family enjoying a delicious meal together inside a cozy fine-dining restaurant. Warm inviting ambient lighting, smiling faces, authentic reactions, beautifully served food on the table, slow and smooth camera pan across the table, hyper-detailed environment.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "عائلة عربية تستمتع بتناول وجبة فاخرة معًا داخل مطعم دافئ وراقي، إضاءة محيطة دافئة وجذابة، وجوه مبتسمة وتفاعلات عفوية حقيقية، الأطباق منسقة بشكل جميل على الطاولة، حركة كاميرا أفقية بطيئة وسلسة، تفاصيل واقعية للمكان."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "mall_scene": {
        "type": "example",
        "message": (
            "🛍️ Mall Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic wide medium shot of an Arabic couple walking and shopping together inside a modern luxury shopping mall. Bright clean commercial lighting, storefronts softly blurred in the background, happy casual conversation, slow tracking camera movement in front of them, hyper-realistic.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "لقطة متوسطة واسعة لشاب وفتاة عربيين يتسوقان معًا داخل مول تجاري حديث وفاخر، إضاءة المكان مشرقة ونظيفة، واجهات المحلات تظهر بلور (مغبشة) ناعم في الخلفية، حديث ودي سعيد، حركة كاميرا بطيئة أمامهما تابعهما بواقعية."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "boxing_scene": {
        "type": "example",
        "message": (
            "🥊 Boxing Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic dynamic close-up of an Arabic boxer training intensely, punching a heavy bag inside a gritty boxing gym. Sweat spraying from the bag impact, intense focused eyes, dramatic high-contrast lighting, slow motion effect on the punch, hyper-realistic grit and texture.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "لقطة قريبة وديناميكية لملاكم عربي يتمرن بقوة ويضرب كيس الملاكمة الثقيل داخل جيم كلاسيكي، العرق المتناثر مع قوة الضربات، عيون مركزة وحادة، إضاءة درامية بتباين عالي، تأثير حركة بطيئة (Slow motion) مع الضربة، واقعية خشونة المشهد."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "street_food_scene": {
        "type": "example",
        "message": (
            "🌮 Street Food Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic close-up of an Arabic young man eating traditional street food at a vibrant street cart in Cairo at night. Steam rising from the fresh food, warm glowing lights of the food cart, joyful satisfied expression, shallow depth of field, slow and steady camera movement, highly realistic details.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "لقطة قريبة لشاب عربي يأكل طعام شارع تقليدي من عربة أكل حيوية في القاهرة ليلًا، البخار يتصاعد من الأكل الطازج، إضاءة دافئة وجذابة من أضواء العربة، تعبيرات وجه سعيدة وممتنة، عزل قوي للخلفية، حركة كاميرا بطيئة وثابتة."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "train_scene": {
        "type": "example",
        "message": (
            "🚆 Train Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic close-up profile shot of an Arabic man sitting thoughtfully next to a train window, looking out as landscapes pass by. Soft natural daylight changing dynamically, detailed facial features, slow subtle camera pan inside the cabin, cinematic realism, melancholic moody atmosphere.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "لقطة جانبية قريبة لرجل عربي يجلس بتأمل بجانب نافذة القطار، ينظر للخارج مع حركة المناظر الطبيعية المارة، إضاءة نهارية طبيعية ناعمة تتغير ديناميكياً، ملامح وجه تفصيلية، حركة كاميرا خفيفة وبطيئة داخل الكابينة، أجواء واقعية هادئة."
        ),
        "options": [{"id": "examples", "title": "💡 كل الأمثلة"}]
    },

    "exam_scene": {
        "type": "example",
        "message": (
            "📝 Exam Scene\n\n"
            "🇺🇸 English Prompt:\n"
            "Cinematic tight close-up of a stressed Arabic student studying intensely before exams late at night at his desk. Holding a pen, notes and books piled up, lit by a single warm desk lamp, deep focus and tired eyes, slow subtle camera push-in, hyper-detailed realistic environment.\n\n"
            "🇪🇬 Arabic Prompt:\n"
            "لقطة قريبة جداً لطالب عربي يذاكر بتركيز وإجهاد قبل الامتحانات في وقت متأخر من الليل على مكتبه، يمسك قلماً والكتب والمذكرات متراكمة حوله، يضيئه أباجورة مكتب دافئة واحدة، عيون متعبة ومركزة، زووم سينمائي خفيف وبطيء جدًا."
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