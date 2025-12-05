from configparser import ConfigParser


class Config:
    def __init__(self, config_file='src/langgraphagenticai/ui/uiconfigfile.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        # 🔴 THIS is the only real change: always return a string
        return self.config.get(
            "DEFAULT",               # section name from your INI: [Default]
            "PAGE_TITLE",            # key name from your INI
            fallback="LangGraph: Build Stateful Agentic AI Graph"
        )
