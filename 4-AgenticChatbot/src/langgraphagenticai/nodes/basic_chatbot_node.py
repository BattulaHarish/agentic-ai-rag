from src.langgraphagenticai.state.state import State


class BasicChatbotNode:
    """
    Basic chatbot login Implementation
    """
    def __init__(self,model):
        self.llm=model

    def process(self,state:State)->dict:
        """
        This function is used to chat with the user
        """
        return{"messages":self.llm.invoke(state["messages"])}