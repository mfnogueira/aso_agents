from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
from crewai_tools import ScrapeWebsiteTool
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('GROQ_API_KEY')
model_name = os.getenv('MODEL', 'llama3-8b-8192')
default_llm = ChatGroq(groq_api_key=api_key, model=model_name)

search_tool = ScrapeWebsiteTool()

writer = Agent(
    role='Writer',
    goal='Escrever artigos envolventes sobre {topic}',
    tool=[search_tool],
    llm=default_llm,
    verbose=True,
    backstory="Você é um ótimo escritor para descrever adequadamente qualquer assunto fornecido de forma clara e objetiva."
)

write_task = Task(
    description=(
        "Escreva um artigo detalhado sobre as tendências atuais em inteligência artificial "
        "O artigo deve ser informativo e cativante, visando a clareza e acessibilidade para leitores não especializados."
    ),
    expected_output="Um artigo de 500 palavras em formato csv em português.",
    agent=writer,
    output_file='artigo-sobre-IA.csv'
)

crew = Crew(agents=[writer], tasks=[write_task], verbose =True)

result = crew.kickoff(inputs={'topic': 'Inteligência Artificial'})
print(result)
